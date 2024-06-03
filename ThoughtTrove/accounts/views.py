from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def create_account(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    password1 = request.POST['password1']

    if password == password1:
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email taken')
            return redirect('/register')
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            return redirect('/login')
    else:
        messages.info(request, "Passwords don't match")
        return redirect('/register')
    
def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/main')
    else:
        messages.info(request, 'invalid credentials')
        return redirect('/login')
    
def logout(request):
    auth.logout(request)
    return redirect('/')