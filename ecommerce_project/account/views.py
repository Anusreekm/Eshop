from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth



# Create your views here.

def registration(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username=request.POST['username']
        email = request.POST['email']
        user_password= request.POST['user_password']
        confirm_password=request.POST['confirm_password']

        if user_password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('account:registration')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=user_password)
                user.save()
                print("User created")
        else:
            messages.info(request, "password not matched")
            print("password not matched")
            return redirect('account:registration')
        return redirect('/')
    else:

        return render(request,'registration.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Unauthorised User')
            return redirect('account:login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

