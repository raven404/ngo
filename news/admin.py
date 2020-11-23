from django.contrib import admin
from .models import Category, News, NewsView, video
# Register your models here.
admin.site.register(Category)
admin.site.register(NewsView)
admin.site.register(News)
admin.site.register(video)
