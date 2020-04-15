from django.urls import path
from .import views
from subscribe.views import email_list_signup
app_name = 'src'

urlpatterns = [
    # path('',views.index, name='home'),
    # path('blog/',views.blog, name='blog'),
    path('', views.IndexView.as_view(), name='home'),
    # path('blog/', post_list, name='post-list'),
    path('blog/', views.PostListView.as_view(), name='post-list'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('team/',views.team, name='team'),
    path(r'pay/',views.pay, name='pay'),
    path(r'success/',views.success, name='success'),
    path(r'failure/',views.failure, name='failure'),

    # # # # #path('email-signup/', email_list_signup, name='email-list-signup'),
    # # # # # path('create/', post_create, name='post-create'),
    # # # # path('create/', views.PostCreateView.as_view(), name='post-create'),
    # # # # # path('post/<id>/', post_detail, name='post-detail'),
    # # # # path('post/<pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # # # # # path('post/<id>/update/', post_update, name='post-update'),
    # # # # path('post/<pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    # # # # # path('post/<id>/delete/', post_delete, name='post-delete'),
    # # # # path('post/<pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

]