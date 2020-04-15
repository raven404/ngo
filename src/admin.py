from django.contrib import admin
from .models import Author, Category, Post,Comment,PostView,Team,TeamView

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(TeamView)
admin.site.register(Team)