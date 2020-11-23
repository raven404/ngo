from django.contrib import admin

# Register your models here.
from .models import Category, Community, CommunityView, CommunityImage, CommunityPost, CommunityPostImage


class CommunityImageAdmin(admin.StackedInline):
    model = CommunityImage


class CommunityPostImageAdmin(admin.StackedInline):
    model = CommunityPostImage


class CommunityPostAdmin(admin.StackedInline):
    inlines = [CommunityPostImageAdmin]
    model = CommunityPost


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    inlines = [CommunityImageAdmin, CommunityPostAdmin]

    class Meta:
        model = Community


# @admin.register(CommunityImage)
# class CommunityImageAdmin(admin.ModelAdmin):
#     pass


@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
    inlines = [CommunityPostImageAdmin]
    model = CommunityPost


# @admin.register(CommunityPostImage)
# class CommunityPostImageAdmin(admin.ModelAdmin):
#     pass


# admin.site.register(Author)
admin.site.register(Category)
# admin.site.register(Event)
# admin.site.register(CommunityView)
# admin.site.register(Image)
# admin.site.register(CommunityAdmin)
