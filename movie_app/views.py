from logging import raiseExceptions

from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response

from .serializers  import *
from .models import *
from .permissions import CheckStatus, CheckUserRating
from .pagination import GenrePagination
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid.save()
        user = serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные денные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializers.validated_data
        return Response(serializers.data, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class =  ProfileSerializers

    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)
    permission_classes = [permissions.IsAuthenticated]

class ProfileEditAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class =  ProfileSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)

class CountryListAPIView (generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class =  CountrySerializers
    permission_classes = [permissions.IsAuthenticated]

class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializers
    permission_classes = [permissions.IsAuthenticated]

class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class =  ActorSerializers
    permission_classes = [permissions.IsAuthenticated]


class ActorDetailAPIView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class =  ActorDetailSerializers
    permission_classes = [permissions.IsAuthenticated]


class DirectorViewSet (viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class =  DirectorSerializers
    permission_classes = [permissions.IsAuthenticated]

class GenreViewSet (viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class =  GenreSerializers
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = GenrePagination

class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializers
    permission_classes = [permissions.IsAuthenticated]

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializers
    permission_classes = [permissions.IsAuthenticated, CheckStatus]

class RatingViewSet (viewsets.ModelViewSet):
    queryset =Rating.objects.all()
    serializer_class =  RatingSerializers
    permission_classes = [CheckUserRating]
    permission_classes = [permissions.IsAuthenticated]

class FavouriteViewSet (viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class =  FavouriteSerializers

class FavouriteItemViewSet (viewsets.ModelViewSet):
    queryset = FavouriteMovie.objects.all()
    serializer_class =  FavouriteItemSerializers
    permission_classes = [permissions.IsAuthenticated]

class HistoryViewSet (viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class =  HistorySerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return History.objects.filter(user=self.request.user)



