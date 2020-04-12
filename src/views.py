from django.shortcuts import render, get_object_or_404 , redirect, reverse
from django.http import HttpResponse , HttpResponseRedirect, Http404
from .models import Post, Author, PostView
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators import csrf
from .forms import CommentForm, PostForm
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from subscribe.forms import EmailSignupForm
from subscribe.models import Signup

# Create your views here.

form = EmailSignupForm()

def get_author(user):
    author = Author.objects.filter(user=user)
    if author.exists():
        return author[0]
    return None

class IndexView(View):
    form = EmailSignupForm()

    def get(self, request, *args, **kwargs):
        featured = Post.objects.filter(featured=True)
        latest = Post.objects.order_by('-timestamp')[0:3]
        context = {
            'object_list': featured,
            'latest': latest,
            'form': self.form
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        messages.info(request, "Successfully subscribed")
        return redirect("home")



def index(request):
    programs = Post.objects.filter(featured=True,categories__title__exact = "program").order_by('-timestamp')[0:3]
    projects = Post.objects.filter(featured=True,categories__title__exact = "project").order_by('-timestamp')[0:3]
    sliderview= Post.objects.filter(slider=True ).order_by('-timestamp')[0:3]
    latest = Post.objects.order_by('-timestamp')[0:3]   

    if request.method == "POST": 
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

        
    context = {
        'programs': programs,
        'projects':projects,
        'latest': latest,
        'sliderview':sliderview,
    }

    return render(request,'index.html', context)

class PostListView(ListView):
    form = EmailSignupForm()
    model = Post
    template_name = 'blog.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        #category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        #context['category_count'] = category_count
        context['form'] = self.form
        return context


def post_list(request):
    #category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        #'category_count': category_count,
        'form': form
    }
    return render(request, 'blog.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    form = CommentForm()

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
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'pk': post.pk
            }))


def post_detail(request, id):
    #category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(Post, id=id)

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)

    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': post.pk
            }))
    context = {
        'post': post,
        'most_recent': most_recent,
        #'category_count': category_count,
        'form': form
    }
    return render(request, 'post.html', context)



# def blog(request):
#     return render(request,'blog.html', {})

def about(request):
    return render(request,'about.html', {})

def contact(request):
    return render(request,'contact.html', {})



#PAYMENT GATEEWAY     

def pay(request):
    MERCHANT_KEY = "BXpOVCvl"
    key="BXpOVCvl"                  
    SALT = "0teFcBB5eu"
    PAYU_BASE_URL = "https://sandboxsecure.payu.in/_payment"
    action = ''
    posted={}
    # Merchant Key and Salt provided y the PayU.
    for i in request.POST:
        posted[i]=request.POST[i]
    hash_object = hashlib.sha256(str(b'randint(0,20)').encode('utf-8'))
    txnid=hash_object.hexdigest()[0:20]
    hashh = ''
    posted['txnid']=txnid
    hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
    posted['key']=key
    hash_string=''
    hashVarsSeq=hashSequence.split('|')
    for i in hashVarsSeq:
        try:
            hash_string+=str(posted[i])
        except Exception:
            hash_string+=''
        hash_string+='|'
    hash_string+=SALT
    hashh=hashlib.sha512((hash_string).encode('utf-8')).hexdigest().lower()
    action = PAYU_BASE_URL
    if(posted.get("key")!=None and posted.get("txnid")!=None and posted.get("productinfo")!=None and posted.get("firstname")!=None and posted.get("email")!=None):
        return render(request,'current_datetime.html',{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"https://sandboxsecure.payu.in/_payment" })
    else:
        return render(request,'current_datetime.html',{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"." })

@csrf_protect
@csrf_exempt
def success(request):
    c = {}
    status=request.POST["status"]
    firstname=request.POST["firstname"]
    amount=request.POST["amount"]
    txnid=request.POST["txnid"]
    posted_hash=request.POST["hash"]
    key=request.POST["key"]
    productinfo=request.POST["productinfo"]
    email=request.POST["email"]
    salt=""
    try:
        additionalCharges=request.POST["additionalCharges"]
        retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    except Exception:
        retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    hashh=hashlib.sha512((retHashSeq).encode('utf-8')).hexdigest().lower()
    if(hashh !=posted_hash):
        print ("Invalid Transaction. Please try again")
    else:
        print ("Thank You. Your order status is ", status)
        print ("Your Transaction ID for this transaction is ",txnid)
        print ("We have received a payment of Rs. ", amount ,". Your order will soon be shipped.")
    return render(request,'sucess.html',{"txnid":txnid,"status":status,"amount":amount,})


@csrf_protect
@csrf_exempt
def failure(request):
    c = {}
    status=request.POST["status"]
    firstname=request.POST["firstname"]
    amount=request.POST["amount"]
    txnid=request.POST["txnid"]
    posted_hash=request.POST["hash"]
    key=request.POST["key"]
    productinfo=request.POST["productinfo"]
    email=request.POST["email"]
    salt=""
    try:
        additionalCharges=request.POST["additionalCharges"]
        retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    except Exception:
        retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    hashh=hashlib.sha512((retHashSeq).encode('utf-8')).hexdigest().lower()
    if(hashh !=posted_hash):
        print ("Invalid Transaction. Please try again")
    else:
        print ("Thank You. Your order status is ", status)
        print ("Your Transaction ID for this transaction is ",txnid)
        print ("We have received a payment of Rs. ", amount ,". Your order will soon be shipped.")
    return render(request,"Failure.html",c)
