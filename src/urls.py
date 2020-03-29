from django.urls import path
from .import views
app_name = 'src'

urlpatterns = [
    path('',views.index, name='home'),
    path('blog/',views.blog, name='blog'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path(r'^pay/',views.Pay, name='pay'),
    path(r'^Success/',views.success, name='success'),
    path(r'^Failure/',views.failure, name='failure'),

]