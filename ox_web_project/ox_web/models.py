from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify

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
  author = models.CharField(max_length=100)
  posted = models.DateTimeField(default=timezone.now)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Blog, self).save(*args, **kwargs)

  def __unicode__(self):
    return "{0}".format(self.title)

class Job(models.Model):
  author = models.CharField(max_length=100)
  created_at = models.DateTimeField(default=timezone.now)
  data_path = models.CharField(max_length=200)
  output_path = models.CharField(max_length=200)
