from django.urls import path
from .import views
app_name = 'community'

urlpatterns = [

    path('Nandlal-community/', views.Nandlal, name='NandlalCommunity'),
    path('Badabagh-community/', views.Badabagh, name='BadabaghCommunity'),
]
