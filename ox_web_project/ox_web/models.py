from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
  user = models.OneToOneField(User)
  website = models.URLField(blank=True)
  
  def __unicode__(self):
    return self.user.username

class Blog(models.Model):
  title = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(max_length=100, unique=True)
  body = models.TextField()
  posted = models.DateTimeField(default=timezone.now)

  def __unicode__(self):
    return "{0}".format(self.title)

