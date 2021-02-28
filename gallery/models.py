from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    artist_description = models.CharField(max_length=280)

    def __str__(self):
        return str(self.user)


class Collection(models.Model):
    collection_name = models.CharField(max_length=50)
    collection_description = models.CharField(max_length=280)

    def __str__(self):
        return str(self.collection_name)


class Artwork(models.Model):
    artist_name = models.ForeignKey('Artist', on_delete=models.CASCADE)
    artwork_title = models.CharField(max_length=50)
    artwork_description = models.CharField(max_length=280)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.artist_name)


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_description = models.CharField(max_length=280)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.tag_name)


class Rating(models.Model):
    rating_level = models.IntegerField(default=5)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()
