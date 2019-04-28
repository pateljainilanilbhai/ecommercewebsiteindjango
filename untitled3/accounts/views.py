from django.shortcuts import render, redirect, HttpResponseRedirect,HttpResponse
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm,useraddaddressform
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Address

import re
# Create your views here.
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(username=request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('profile'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)

def register(request):



    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                
                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect('index')
            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)
    
@login_required
def profile(request):
    return render(request, 'profile.html')

def addaddress(request):
    if request.method == 'POST':
        user_form = useraddaddressform(request.POST or None)
        if user_form.is_valid():
            username=request.user
            a=Address()

            listl=[]
            for i in user_form.cleaned_data.items():
                listl.append(i[1])
            a.user_id = username
            a.full_name = listl[0]
            a.phone_number = listl[1]
            a.country = listl[2]
            a.postcode = listl[3]
            a.town_or_city = listl[4]
            a.street_address_1 = listl[5]
            a.street_address_2 = listl[6]
            a.county = listl[7]
            a.save()
            return render(request, 'profile.html')
    else:
        user_form = useraddaddressform()

    args = {"form":user_form}
    return render(request, 'accounts/address_form.html', args)

