from django.contrib import admin

from .models import Artist, Artwork, Favorite, Collection, Rating


class ArtistList(admin.ModelAdmin):
    list_display = ('user_name', 'artist_description')
    list_filter = ('user_name', 'artist_description')
    search_fields = ('user_name',)
    ordering = ['user_name']


class ArtworkList(admin.ModelAdmin):
    list_display = ('artist_name', 'artwork_title', 'artwork_description')
    list_filter = ('artist_name', 'artwork_title')
    search_fields = ('artist_name',)
    ordering = ['artist_name']


class FavoriteList(admin.ModelAdmin):
    list_display = ('user_name', 'artwork_name')
    list_filter = ('user_name', 'artwork_name')
    search_fields = ('user_name',)
    ordering = ['user_name']


class CollectionList(admin.ModelAdmin):
    list_display = ('user_name', 'collection_name', 'collection_description')
    list_filter = ('user_name', 'collection_name')
    search_fields = ('user_name',)
    ordering = ['user_name']


class RatingList(admin.ModelAdmin):
    list_display = ('user_name', 'rating_level', 'artwork_name')
    list_filter = ('user_name', 'artwork_name')
    search_fields = ('user_name',)
    ordering = ['user_name']


admin.site.register(Artist, ArtistList)
admin.site.register(Artwork, ArtworkList)
admin.site.register(Favorite, FavoriteList)
admin.site.register(Collection, CollectionList)
admin.site.register(Rating, RatingList)
