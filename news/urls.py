from django.urls import path
from .import views
app_name = 'news'

urlpatterns = [

    # path('Nandlal-community/', views.Nandlal, name='NandlalCommunity'),
    # path('Badabagh-community/', views.Badabagh, name='BadabaghCommunity'),
    path('media/', views.media, name='media'),

]
