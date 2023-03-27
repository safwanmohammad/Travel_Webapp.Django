from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(req):
    if req.method == 'POST':
        username = req.POST['user_name']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('/')
        else:
            messages.info(req, 'invalid credential')
            return redirect('login')
    return render(req, 'login.html')


def register(req):
    if req.method == 'POST':
        user_name = req.POST['user_name']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        email = req.POST['email']
        password = req.POST['password']
        confirm_password = req.POST['confirm_password']

        if password == confirm_password:

            if User.objects.filter(username=user_name).exists():
                messages.info(req, 'Oops UserName already taken')
                print("Oops UserName already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(req, 'Oops email already taken')
                return redirect('register')
            else:

                user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password)
                user.save();
            print("User_Created")
            return redirect('login')
        else:
            print("password not matching")
            messages.info(req, 'password not matching')
            return redirect('register')

    return render(req, 'register.html')


def logout(req):
    auth.logout(req)
    return redirect('/')
