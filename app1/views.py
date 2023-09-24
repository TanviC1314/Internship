from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from app1.models import FilesUpload
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')

def HomePage(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file2 = request.FILES.getlist('file')[1]
        document = FilesUpload.objects.create(file=file2)
        document.save()
        messages.success(request, "File Uploaded Sucessfully")
    return render (request,'home.html')

def IndexPage(request):
    return render (request,'index.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            messages.success(request, "Your password and confrom password are not Same!!")
            return redirect('signup')
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request, "Username or Password is incorrect!")
            return redirect('login')

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')