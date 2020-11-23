from django.urls import path
from .import views
# from subscribe.views import email_list_signup
app_name = 'posts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    # path('', views.index, name='home'),
    path('program/', views.ProgramListView.as_view(), name='post-list'),
    path('project/', views.ProjectListView.as_view(), name='post-list'),
    path('campus/', views.CampusListView.as_view(), name='post-list'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),





]
