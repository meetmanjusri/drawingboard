from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    user_username = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=100)
    user_firstname = models.CharField(max_length=50)
    user_lastname = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user_username)

    class Meta:
        abstract = True


class Artist(User):
    artist_description = models.CharField(max_length=280)


class Collection(models.Model):
    collection_name = models.CharField(max_length=50)
    collection_description = models.CharField(max_length=280)
    # collection_user_username = models.ForeignKey(User,related_name='%(class)s_related',
    # on_delete=models.CASCADE)


class Artwork(models.Model):
    artwork_title = models.CharField(max_length=50)
    artwork_description = models.CharField(max_length=280)


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_description = models.CharField(max_length=280)


class Rating(models.Model):
    rating_level = models.IntegerField;
