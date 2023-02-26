from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', blank=True, null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    username = models.CharField(max_length=25, blank=True, null=True, unique=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField()
    company_name = models.CharField(max_length=164)
    country = models.CharField(max_length=35, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    time_created = models.DateTimeField(auto_now=True)


class Post(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, verbose_name="User")
    job_title = models.CharField(max_length=120)
    job_type = models.CharField(max_length=120)
    skills = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    is_remote = models.BooleanField(default=False)
    description = RichTextField()
    company_name = models.CharField(max_length=164, blank=True)
    website = models.CharField(max_length=512)

    def save(self, *args, **kwargs):
        self.company_name = self.user.company_name
        super(Post, self).save(*args, **kwargs)
