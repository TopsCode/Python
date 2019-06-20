from django.shortcuts import render
from .models import * 

# Create your views here.

def home(request):
    return render(request,"profile_app/user_registration.html")

def storedata(request):
    f_name=request.POST['fname']
    l_name=request.POST['lname']
    mobile=request.POST['mobile']
    profile_pic=request.FILES['profile_pic']
    usernew=user.objects.create(firstname=f_name,lastname=l_name,mobile=mobile,profile_pic=profile_pic)
    return render(request,"profile_app/user_profile.html",{'usernew':usernew})