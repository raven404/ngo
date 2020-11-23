from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
from subscribe.forms import EmailSignupForm
from subscribe.models import Signup
# from .forms import CommentForm, PostForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import News, NewsView, video
import datetime
# Create your views here.
from posts.models import Post, Author, PostView, Team, TeamView

now = datetime.datetime.now()
latest = Post.objects.order_by('-timestamp')[0:9]
most_view = sorted(Post.objects.all(),
                   key=lambda t: t.view_count, reverse=True)[0:4]
form = EmailSignupForm()
News = News.objects.all()
video = video.objects.all()
sliderview = News.filter(
    slider=True).order_by('-timestamp')[0:6]


def media(request):
    print(News)
    print("Welcome")
    print(most_view[1])

    return render(request, 'Media.html', {'now': now, 'latest': News, 'video': video, 'sliderview': sliderview, 'form': form, 'most': most_view})
