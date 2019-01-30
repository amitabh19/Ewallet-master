from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserCreationForm, ProfileForm
from django.contrib.messages import constants as messages
from django.contrib.auth.models import User
from . models import User,UserProfile
from django.db import connection

def index(request):
    return HttpResponse("namaste beta")

'''
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save() and profile_form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return HttpResponse("namaste beta")
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'wallet/signup.html', {'form': form, 'profile_form': profile_form},
                  )
'''


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, )
        profile_form = ProfileForm(request.POST,)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            mobile = profile_form.cleaned_data['mob']
            uname = form.cleaned_data['username']
            u = User.objects.get(username=uname)
            p = UserProfile.objects.get(user_id=u.pk)
            p.mob = mobile
            p.save()

            return HttpResponse('yo yo yo')
        else:
            return HttpResponse('no no no')
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'wallet/signup.html', {
        'form': form,
        'profile_form': profile_form
    })

