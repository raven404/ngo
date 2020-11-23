from django.urls import path
from .import views
app_name = 'donation'

urlpatterns = [

    path(r'donate/', views.pay, name='pay'),
    path(r'success/', views.success, name='success'),
    path(r'failure/', views.failure, name='failure'),
]
