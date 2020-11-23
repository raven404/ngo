from django.urls import path
from .import views
app_name = 'subscribe'

urlpatterns = [
    path('subscribe/', views.email_list_signup, name='subscribe'),
]
