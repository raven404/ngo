from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import get_template
from posts.models import Post, Author, PostView, Team, TeamView
from django.template import Context, Template, RequestContext
from subscribe.forms import EmailSignupForm
from subscribe.models import Signup
# from .forms import CommentForm, PostForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Community, CommunityView, CommunityImage, CommunityPost, CommunityPostImage
import datetime


now = datetime.datetime.now()
latest = Post.objects.order_by('-timestamp')[0:9]
form = EmailSignupForm()
most_view = sorted(Post.objects.all(),
                   key=lambda t: t.view_count, reverse=True)[0:4]
# Create your views here.


def Nandlal(request):
    community = Community.objects.filter(
        Category__title__exact="Nandlal")
    pics = CommunityImage.objects.filter(community=community.first())
    communitypost = CommunityPost.objects.filter(community=community.first())
    communitypostimage = CommunityPostImage.objects.filter(
        communitypost__in=communitypost.all())
    return render(request, 'nandlal.html', {
        'now': now,
        'community': community,
        'pics': pics,
        'post': communitypost,
        'photos': communitypostimage,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def Badabagh(request):
    community = Community.objects.filter(
        Category__title__exact="Badabagh")
    pics = CommunityImage.objects.filter(community=community.first())
    communitypost = CommunityPost.objects.filter(community=community.first())
    communitypostimage = CommunityPostImage.objects.filter(
        communitypost__in=communitypost.all())
    print(communitypostimage[0].images)
    return render(request, 'badabagh.html', {
        'now': now,
        'community': community,
        'pics': pics,
        'post': communitypost,
        'photos': communitypostimage,
        'latest': latest,
        'most': most_view,
        'form': form
    })
