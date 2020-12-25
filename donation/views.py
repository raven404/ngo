from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators import csrf
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from subscribe.forms import EmailSignupForm
from subscribe.models import Signup
from posts.models import Post, Author, PostView, Team, TeamView


now = datetime.datetime.now()
latest = Post.objects.order_by('-timestamp')[0:9]
form = EmailSignupForm()
most_view = sorted(Post.objects.all(),
                   key=lambda t: t.view_count, reverse=True)[0:4]


# Create your views here.

# PAYMENT GATEEWAY


def pay(request):
    MERCHANT_KEY = "BXpOVCvl"
    key = "BXpOVCvl"
    SALT = "0teFcBB5eu"
    PAYU_BASE_URL = "https://sandboxsecure.payu.in/_payment"
    action = ''
    posted = {}
    surl = "http://127.0.0.1:8000/success/"
    furl = "http://127.0.0.1:8000/failure/"

    # Merchant Key and Salt provided y the PayU.
    for i in request.POST:
        posted[i] = request.POST[i]
    hash_object = hashlib.sha256(str(b'randint(0,20)').encode('utf-8'))
    txnid = hash_object.hexdigest()[0:20]
    hashh = ''
    posted['txnid'] = txnid
    hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
    posted['key'] = key
    hash_string = ''
    hashVarsSeq = hashSequence.split('|')
    for i in hashVarsSeq:
        try:
            hash_string += str(posted[i])
        except Exception:
            hash_string += ''
        hash_string += '|'
    hash_string += SALT
    hashh = hashlib.sha512((hash_string).encode('utf-8')).hexdigest().lower()
    action = PAYU_BASE_URL
    if(posted.get("key") != None and posted.get("txnid") != None and posted.get("productinfo") != None and posted.get("firstname") != None and posted.get("email") != None):
        return render(request, 'current_datetime.html', {"posted": posted, "hashh": hashh, "MERCHANT_KEY": MERCHANT_KEY, "txnid": txnid, "hash_string": hash_string,  "surl": surl, "furl": furl, 'most': most_view, 'form': form, "now": now, "latest": latest, "action": "https://sandboxsecure.payu.in/_payment"})
    else:
        return render(request, 'current_datetime.html', {"posted": posted, "hashh": hashh, "MERCHANT_KEY": MERCHANT_KEY, "txnid": txnid, "hash_string": hash_string,  "surl": surl, "furl": furl, 'most': most_view, 'form': form, "now": now, "latest": latest, "action": "."})


@csrf_protect
@csrf_exempt
def success(request):
    c = {}
    status = request.POST["status"]
    firstname = request.POST["firstname"]
    amount = request.POST["amount"]
    txnid = request.POST["txnid"]
    posted_hash = request.POST["hash"]
    key = request.POST["key"]
    productinfo = request.POST["productinfo"]
    email = request.POST["email"]
    salt = ""
    try:
        additionalCharges = request.POST["additionalCharges"]
        retHashSeq = additionalCharges+'|'+salt+'|'+status+'|||||||||||' + \
            email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    except Exception:
        retHashSeq = salt+'|'+status+'|||||||||||'+email+'|' + \
            firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    hashh = hashlib.sha512((retHashSeq).encode('utf-8')).hexdigest().lower()
    if(hashh != posted_hash):
        print("Invalid Transaction. Please try again")
    else:
        print("Thank You. Your order status is ", status)
        print("Your Transaction ID for this transaction is ", txnid)
        print("We have received a payment of Rs. ",
              amount, ". Your order will soon be shipped.")
    return render(request, 'success.html', {"txnid": txnid, "status": status, "amount": amount, 'most': most_view, 'form': form, "now": now, "latest": latest, })


@csrf_protect
@csrf_exempt
def failure(request):
    c = {}
    status = request.POST["status"]
    firstname = request.POST["firstname"]
    amount = request.POST["amount"]
    txnid = request.POST["txnid"]
    posted_hash = request.POST["hash"]
    key = request.POST["key"]
    productinfo = request.POST["productinfo"]
    email = request.POST["email"]
    salt = ""
    try:
        additionalCharges = request.POST["additionalCharges"]
        retHashSeq = additionalCharges+'|'+salt+'|'+status+'|||||||||||' + \
            email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    except Exception:
        retHashSeq = salt+'|'+status+'|||||||||||'+email+'|' + \
            firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    hashh = hashlib.sha512((retHashSeq).encode('utf-8')).hexdigest().lower()
    if(hashh != posted_hash):
        print("Invalid Transaction. Please try again")
    else:
        print("Thank You. Your order status is ", status)
        print("Your Transaction ID for this transaction is ", txnid)
        print("We have received a payment of Rs. ",
              amount, ". Your order will soon be shipped.")
    return render(request, "Failure.html", {'most': most_view, 'form': form, "now": now, "latest": latest, })
