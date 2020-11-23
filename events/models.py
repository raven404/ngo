from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.urls import reverse
from posts.models import Author

User = get_user_model()

# Create your models here.


class EventView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# class EventContentView(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey('EventContent', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


# class Event(models.Model):

#     title = models.CharField(max_length=100, default="Enter The Title")
#     Category = models.ManyToManyField(Category)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     view_count = models.IntegerField(default=0)
#     content = HTMLField(default="Write Down The Content Here")
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     # thumbnail = models.ImageField()

#     # previous_post = models.ForeignKey(
#     #     'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
#     # next_post = models.ForeignKey(
#     #     'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse('posts:post-detail', kwargs={
#             'pk': self.pk
#         })

#     def get_update_url(self):
#         return reverse('posts:post-update', kwargs={
#             'pk': self.pk
#         })

#     def get_delete_url(self):
#         return reverse('posts:post-delete', kwargs={
#             'pk': self.pk
#         })

#     # @property
#     # def get_comments(self):
#     #     return self.comments.all().order_by('-timestamp')

#     # @property
#     # def comment_count(self):
#     #     return Comment.objects.filter(post=self).count()

#     @property
#     def view_count(self):
#         return PostView.objects.filter(post=self).count()


# class EventContent(models.Model):

#     title = models.CharField(max_length=100, default="Enter The Title")
#     Category = models.ManyToManyField(Category)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     content = HTMLField()
#     view_count = models.IntegerField(default=0)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse('posts:post-detail', kwargs={
#             'pk': self.pk
#         })

#     def get_update_url(self):
#         return reverse('posts:post-update', kwargs={
#             'pk': self.pk
#         })

#     def get_delete_url(self):
#         return reverse('posts:post-delete', kwargs={
#             'pk': self.pk
#         })

#     @property
#     def view_count(self):
#         return PostView.objects.filter(post=self).count()


def get_image_filename(instance, filename):
    id = instance.event.id
    return "event_images/%s" % (id)


# class Image(models.Model):
#     event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
#     slider = models.BooleanField()
#     image = models.ImageField(upload_to=get_image_filename,
#                               verbose_name='Image')
# class Image(models.Model):
#     event = models.ForeignKey(
#         Event, related_name='images', on_delete=models.CASCADE)
#     Image = models.ImageField(upload_to='upload', default="NULL")
#     slider = models.BooleanField(default=False)

#     def __str__(self):
#         return '%s - %s ' % (self.event, self.file)


class Event(models.Model):

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


class EventImage(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.event.title
