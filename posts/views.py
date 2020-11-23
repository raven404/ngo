from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import get_template
from .models import Post, Author, PostView, Team, TeamView
from django.template import Context, Template, RequestContext
from subscribe.forms import EmailSignupForm
from subscribe.models import Signup
from .forms import CommentForm, PostForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import datetime


now = datetime.datetime.now()
latest = Post.objects.order_by('-timestamp')[0:9]
form = EmailSignupForm()
most_view = sorted(Post.objects.all(),
                   key=lambda t: t.view_count, reverse=True)[0:4]


def get_author(user):
    author = Author.objects.filter(user=user)
    if author.exists():
        return author[0]
    return None


class IndexView(View):
    # form = EmailSignupForm()

    def get(self, request, *args, **kwargs):
        programs = Post.objects.filter(
            featured=True, categories__title__exact="program").order_by('-timestamp')[0:3]
        projects = Post.objects.filter(
            featured=True, categories__title__exact="project").order_by('-timestamp')[0:3]
        sliderview = Post.objects.filter(
            slider=True).order_by('-timestamp')[0:3]
        campus = Post.objects.filter(
            featured=True, categories__title__exact="campus").order_by('-timestamp')[0:3]
        form = EmailSignupForm()

        context = {
            'programs': programs,
            'projects': projects,
            'sliderview': sliderview,
            'campus': campus,
            'latest': latest,
            'now': now,
            'most': most_view,
            'form': form
        }

        return render(request, 'index.html', context)


class ProgramListView(ListView):
    form = EmailSignupForm()
    queryset = Post.objects.filter(
        categories__title__exact="program").order_by('timestamp')
    template_name = 'program.html'
    context_object_name = 'queryset'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        #category_count = get_category_count()
        #posts=Post.objects.filter(categories__title__exact = "program").order_by('timestamp')
        #most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        #context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        #context['category_count'] = category_count
        context['form'] = self.form
        # context['posts']=posts
        header = "PROGRAMS"
        context['header'] = header
        context['now'] = now
        context['latest'] = latest
        context['most'] = most_view
        return context


class ProjectListView(ListView):
    form = EmailSignupForm()
    queryset = Post.objects.filter(
        categories__title__exact="project").order_by('timestamp')
    template_name = 'program.html'
    context_object_name = 'queryset'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        #category_count = get_category_count()
        #posts=Post.objects.filter(categories__title__exact = "program").order_by('timestamp')
        #most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        #context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        #context['category_count'] = category_count
        context['form'] = self.form
        # context['posts']=posts
        header = "PROJECTS"
        context['header'] = header
        context['now'] = now
        context['latest'] = latest
        context['most'] = most_view
        return context


class CampusListView(ListView):
    form = EmailSignupForm()
    queryset = Post.objects.filter(
        categories__title__exact="campus").order_by('timestamp')
    template_name = 'program.html'
    context_object_name = 'queryset'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        #category_count = get_category_count()
        #posts=Post.objects.filter(categories__title__exact = "program").order_by('timestamp')
        #most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        #context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        #context['category_count'] = category_count
        context['form'] = self.form
        # context['posts']=posts
        header = "CAMPUS"
        context['header'] = header
        context['now'] = now
        context['latest'] = latest
        context['most'] = most_view
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    # form_class={
    #             'comment': CommentForm(),
    #             'form'   : EmailSignupForm()
    #             }

    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(
                user=self.request.user,
                post=obj
            )

        return obj

    def get_context_data(self, **kwargs):
        #category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        #context['category_count'] = category_count
        context['comment'] = CommentForm()
        context['form'] = form
        context['now'] = now
        context['latest'] = latest
        context['most'] = most_view
        return context

    def post(self, request, *args, **kwargs):
        comment = CommentForm(request.POST)
        if comment.is_valid():
            post = self.get_object()
            comment.instance.user = request.user
            comment.instance.post = post
            comment.save()
            return redirect(reverse("posts:post-detail", kwargs={
                'pk': post.pk
            }))


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        context['now'] = now
        context['latest'] = latest
        context['most'] = most_view
        return context

    def form_valid(self, form):
        form.instance.author = get_author(self.request.user)
        form.save()
        return redirect(reverse("posts:post-detail", kwargs={
            'pk': form.instance.pk
        }))


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        context['now'] = now
        context['latest'] = latest
        context['most'] = most_view
        return context

    def form_valid(self, form):
        form.instance.author = get_author(self.request.user)
        form.save()
        return redirect(reverse("posts:post-detail", kwargs={
            'pk': form.instance.pk
        }))


class PostDeleteView(DeleteView):
    model = Post
    # pk: form.instance.pk
    success_url = '/'
    # template_name = 'post_confirm_delete.html'

    # def get_success_url(self, **kwargs):
    #     # Assuming there is a ForeignKey from Comment to Post in your model
    #     post = Post
    #     results = Post.objects.filter(self.args)
    #     print(results)
    #     self.object = self.get_object()
    #     print(self.object.categories.all())
    #     print(post.categories.all())
    #     route = Post.categories
    #     print("post : ", post)
    #     return redirect(reverse(route))

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


# def index(request):
#     programs = Post.objects.filter(
#         featured=True, categories__title__exact="program").order_by('-timestamp')[0:3]
#     projects = Post.objects.filter(
#         featured=True, categories__title__exact="project").order_by('-timestamp')[0:3]
#     sliderview = Post.objects.filter(slider=True).order_by('-timestamp')[0:3]
#     latest = Post.objects.order_by('-timestamp')[0:3]

#     if request.method == "POST":
#         email = request.POST["email"]
#         new_signup = Signup()
#         new_signup.email = email
#         new_signup.save()

#     context = {
#         'programs': programs,
#         'projects': projects,
#         'latest': latest,
#         'sliderview': sliderview,
#     }

#     return render(request, 'index.html', context)
