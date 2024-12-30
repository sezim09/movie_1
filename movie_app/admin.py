from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

class MovieVideosInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = MovieLanguages
    extra = 1

class MovieMomentsInline(admin.TabularInline):
    model = Moments
    extra = 2



class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieVideosInline, MovieMomentsInline]

@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    inlines = [MovieVideosInline, MovieMomentsInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Country, Director, Actor, Genre)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }





admin.site.register(Profile)
admin.site.register(Rating)
admin.site.register(Favourite)
admin.site.register(FavouriteMovie)
admin.site.register(History)



