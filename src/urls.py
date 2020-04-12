from django.urls import path
from .import views
app_name = 'src'

urlpatterns = [
    # path('',views.index, name='home'),
    # path('blog/',views.blog, name='blog'),
    path('', views.IndexView.as_view(), name='home'),
    # path('blog/', post_list, name='post-list'),
    path('blog/', views.PostListView.as_view(), name='post-list'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path(r'pay/',views.pay, name='pay'),
    path(r'success/',views.success, name='success'),
    path(r'failure/',views.failure, name='failure'),

]