# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from profile.models import Profile

def login_site(request):
    return render(request,'profile/login.html')

def access(request):
    username = request.POST['usuario']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
        #    obj, created = Profile.objects.get_or_create(user=user, defaults={'first_name':user.first_name, 'last_name':user.last_name,'email': user.email})
        #    if created:
        #        obj.save()
            login(request, user)
            return redirect('/')
    return redirect('/home/error/')

def exit(request):
    logout(request)
    return redirect('/')
