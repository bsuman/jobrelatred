from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
"""
Post Table contains the information regarding the post from each user. 
If the user is deleted, then all the posts from that user are also deleted.
"""


class Post(models.Model):
    # allow title to have max length of 200 characters
    title = models.CharField(max_length=200)
    # the date on which the post was created is having date-time datatype and django builtin utils will manage the timezone
    created_on = models.DateTimeField(default=timezone.now)
    # Open text field
    content = models.TextField()
    # If the user is deleted, then all the posts from that user are also deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


