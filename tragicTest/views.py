from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime

# Create your views here.

def index(request):

    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'tragicTest/index.html', context=context_dict)

def registration(request):

    context_dict = {}

    return render(request, 'tragicTest/registration.html', context=context_dict)

def login(request):

    context_dict = {}

    return render(request, 'tragicTest/login.html', context=context_dict)

def category(request):

    context_dict = {}

    return render(request, 'tragicTest/category.html', context=context_dict)

def article(request):

    context_dict = {}

    return render(request, 'tragicTest/article.html', context=context_dict)

def profile(request):

    context_dict = {}

    return render(request, 'tragicTest/profile.html', context=context_dict)

def profile_uploads(request):

    context_dict = {}

    return render(request, 'tragicTest/profile_uploads.html', context=context_dict)

def profile_reviews(request):

    context_dict = {}

    return render(request, 'tragicTest/profile_reviews.html', context=context_dict)

