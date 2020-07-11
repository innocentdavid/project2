from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    author_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, unique=True, null=False, blank=False)
    desc = models.TextField()
    catg = models.CharField(max_length=50, null=True)
    status = models.IntegerField(default='open', max_length=50, null=True)
    img_url = models.CharField(max_length=200, null=True)
    dateTime = models.CharField(max_length=50, null=False, blank=False)
    starting_bid = models.IntegerField(null=False)
    current_bid = models.IntegerField(null=False)

    def __str__(self):
        return self.title


class Bid(models.Model):
    id = models.IntegerField(primary_key=True)
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.listing_id


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.category_name

class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    listing_id = models.ForeignKey(Listings, on_delete=models.SET_NULL, null=True, blank=True)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)