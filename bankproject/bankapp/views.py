from django.contrib import messages,auth
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def index(request):
    return render(request,"base.html")
#def login(request):
    #return render(request,"login.html")
#def signup(request):
    #return render(request,"signup.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['password1']
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User Name Taken")
                return redirect('signup')

            else:
                user=User.objects.create_user(username=username,password=password,)

                user.save();
                return redirect('login')

        else:
            messages.info(request,"Password is Incorrect")
            return redirect('signup')
        return render('/')
    return render(request,"signup.html")


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('')

    return render(request,"login.html")



def newpage(request):
    return render(request,"newpage.html")

def form(request):
  return render(request,"register.html")

def confirmpage(request):
    return render(request,"confirmpage.html")

def about(request):
    return render(request,"homepage.html")
