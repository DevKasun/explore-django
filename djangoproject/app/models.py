from django.db import models
from django.contrib.auth.models import AbstractUser

ARTICLE_STATUS = (
    ("draft", "Draft"),
    ("in progress", "In progress"),
    ("published", "Published")
)

class UserProfile(AbstractUser):
    # add additional fields in here
    pass

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default="")
    word_column = models.IntegerField()
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(max_length=20, choices=ARTICLE_STATUS, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)