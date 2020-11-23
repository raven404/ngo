
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts')),
    path('', include('subscribe.urls', namespace='subscribe')),
    path('', include('events.urls', namespace='events')),
    path('', include('community.urls', namespace='community')),
    path('', include('news.urls', namespace='news')),
    path('', include('donation.urls', namespace='donation')),




    path('tinymce/', include('tinymce.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
