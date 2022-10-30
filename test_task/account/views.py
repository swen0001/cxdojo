from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def signup(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html')
    elif request.method == 'POST':
        # 1- Getting data from the form:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # 2 - Data validation on the server side:
        if password1 != password2:
            messages.error(request, 'Passwords do not match !(')
            return render(request, 'account/signup.html')
        elif User.objects.filter(username=username):
            messages.error(request, 'Such username already exists !(')
            return render(request, 'account/signup.html')
        else:
            # 3 - Registration and authorization
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            login(request, user)
            messages.success(request, 'You are successfully registered !)')
            return redirect('/')


def signin(request):
    if request.method == 'GET':
        return render(request, 'account/signin.html')
    elif request.method == 'POST':
        # 1 - Getting data from the form:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 2 - Authenticate
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.warning(request, 'User not found !(')
            return render(request, 'account/signin.html')
        else:
            login(request, user)
            messages.success(request, 'You have been successfully logged in !)')
            return redirect('/')


def signout(request):
    logout(request)
    messages.info(request, 'You are logged out of your account !')
    return redirect('/')


