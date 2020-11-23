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
from .models import Event, EventView, EventImage
import datetime


now = datetime.datetime.now()
latest = Post.objects.order_by('-timestamp')[0:9]
form = EmailSignupForm()
most_view = sorted(Post.objects.all(),
                   key=lambda t: t.view_count, reverse=True)[0:4]
# Create your views here.


# def blog_view(request):
#     posts = Post.objects.all()
#     return render(request, 'blog.html', {'posts': posts})


# def detail_view(request, id):
#     post = get_object_or_404(Post, id=id)
#     photos = PostImage.objects.filter(post=post)
#     return render(request, 'detail.html', {
#         'post': post,
#         'photos': photos
#     })


def about(request):
    return render(request, 'about.html', {'now': now, 'latest': latest, 'form': form, 'most': most_view, })


def financial_transparency(request):
    return render(request, 'financial_transparency.html', {'now': now, 'latest': latest, 'form': form, 'most': most_view, })


def family(request):
    return render(request, 'mission_Statement.html', {'now': now, 'latest': latest, 'most': most_view, 'form': form})


def Nandlal_Community(request):
    return render(request, 'nandlal.html', {'now': now, 'latest': latest, 'most': most_view, 'form': form})


def Bada_Bagh(request):
    return render(request, 'badabagh.html', {'now': now, 'latest': latest, 'most': most_view, 'form': form})


def Campus_Engagement(request):
    event = Event.objects.filter(
        Category__title__exact="Campus_Engagement")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'campus_engagement.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def Awareness_Program(request):
    event = Event.objects.filter(
        Category__title__exact="Awareness_Program")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'awareness.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def Relief_Funds(request):
    event = Event.objects.filter(
        Category__title__exact="Relief_Fund")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'relief.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def Co_Curricular_Activities(request):
    event = Event.objects.filter(
        Category__title__exact="Co_Curricular_Activities")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'co_curricular.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def Child_Sponsorship_Program(request):
    event = Event.objects.filter(
        Category__title__exact="Child_Sponsorship_Program")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'CSP.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def Field_Visit(request):
    event = Event.objects.filter(
        Category__title__exact="Field_Visit")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'field_visit.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def Blanket_Drive(request):
    event = Event.objects.filter(
        Category__title__exact="Blanket_Drive")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'blanket_drive.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def Medical_Camp(request):
    event = Event.objects.filter(
        Category__title__exact="Medical_Camp")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'medical_camp.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def media(request):
    return render(request, 'Media.html', {'now': now, 'latest': latest, 'most': most_view, 'form': form})


def chat_over_coffee(request):
    event = Event.objects.filter(
        Category__title__exact="Chat_Over_Coffee")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'COC.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def focal_point(request):
    event = Event.objects.filter(
        Category__title__exact="Focal_Point")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'focalpoint.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def forums(request):
    event = Event.objects.filter(
        Category__title__exact="Forums")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'forums.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def music(request):
    event = Event.objects.filter(
        Category__title__exact="Musical_Concerts")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'music.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form

    })


def language(request):
    event = Event.objects.filter(
        Category__title__exact="English_Class")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'language.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def Alumni(request):
    event = Event.objects.filter(
        Category__title__exact="Alumni")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'Alumni.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def Internships(request):
    event = Event.objects.filter(
        Category__title__exact="Internship")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'Internship.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def Volunteer(request):
    event = Event.objects.filter(
        Category__title__exact="Volunteer")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'volunteers.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def donation(request):
    return render(request, 'Donation.html', {'now': now, 'latest': latest})


def Impact(request):
    event = Event.objects.filter(
        Category__title__exact="Impact_And_Outreach")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'impact.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def Success_Stories(request):
    event = Event.objects.filter(
        Category__title__exact="Success_Stories")
    pics = EventImage.objects.filter(event=event.first())
    return render(request, 'Success_stories.html', {
        'now': now,
        'event': event,
        'pics': pics,
        'latest': latest,
        'most': most_view,
        'form': form
    })


def contact(request):
    return render(request, 'contact.html', {'now': now, 'latest': latest, 'most': most_view, 'form': form})


def team(request):
    team = Team.objects.filter(
        categories__title__exact="team").order_by('-timestamp')
    context = {
        'team': team,
        'now': now,
        'latest': latest,
        'most': most_view,
        'form': form
    }

    return render(request, 'team.html', context)


# def impact(request):
#     impact = Team.objects.filter(
#         categories__title__exact="impact").order_by('-timestamp')
#     context = {
#         'impact': impact,
#         'now': now,
#         'latest': latest
#     }

#     return render(request, 'impact.html', context)


def faqs(request):
    return render(request, 'FAQs.html', {'now': now, 'latest': latest, 'most': most_view, 'form': form})
