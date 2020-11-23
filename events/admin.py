from django.contrib import admin

# Register your models here.
from .models import Category, Event, EventView, EventImage


class EventImageAdmin(admin.StackedInline):
    model = EventImage


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageAdmin]

    class Meta:
        model = Event


@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Author)
admin.site.register(Category)
# admin.site.register(Event)
admin.site.register(EventView)
# admin.site.register(Image)
