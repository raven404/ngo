from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.urls import reverse
from posts.models import Author

User = get_user_model()

# Create your models here.


class CommunityView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Community', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Community(models.Model):

    title = models.CharField(max_length=100, default="Enter The Title")
    Category = models.ManyToManyField(Category)
    timestamp = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    content = HTMLField(default="Write Down The Content Here")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # image = models.FileField(blank=True)

    def __str__(self):
        return self.title

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()


class CommunityImage(models.Model):
    community = models.ForeignKey(
        Community, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='Community/')

    def __str__(self):
        return self.community.title


class CommunityPost(models.Model):
    community = models.ForeignKey(
        Community, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Enter The Title")
    Category = models.ManyToManyField(Category)
    timestamp = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    content = HTMLField(default="Write Down The Content Here")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.title} {0.community.title}'
        return template.format(self)


class CommunityPostImage(models.Model):
    communitypost = models.ForeignKey(
        CommunityPost, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='community/post/')

    def __str__(self):
        template = '{0.communitypost.title}'
        return template.format(self)
