from django.shortcuts import render
from .models import *
from django.core.mail import send_mail

# Create your views here.

def index(request):
    if "a_email" in request.session: 
        uid=Product_Manager.objects.get(email=request.session['a_email'])
        return render(request,"adminpanel/index.html",{'uid':uid})
    else:
        return render(request,"adminpanel/sign-in.html")
    
def signup_page(request):
    if "a_email" in request.session: 
        uid=Product_Manager.objects.get(email=request.session['a_email'])
        return render(request,"adminpanel/index.html",{'uid':uid})
    
    return render(request,"adminpanel/sign-up.html")

def register_product_manager(request):
    try:
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        brandname=request.POST['brandname']
      
        uid=Product_Manager.objects.create(name=name,email=email,password=password,brandname=brandname)
        print("---------------->uid",uid)
        if uid:
            s_msg="successfully registered"
            return render(request,"adminpanel/sign-up.html",{'s_msg':s_msg})
        else:
            e_msg="Invalid input"
            return render(request,"adminpanel/sign-up.html",{'e_msg':e_msg})
    except:
        e_msg="Invalid input"
        return render(request,"adminpanel/sign-up.html",{'e_msg':e_msg})

def admin_login_page(request):
    return render(request,"adminpanel/sign-in.html")

def login_evalute(request):
    if "a_email" in request.session:
        uid=Product_Manager.objects.get(email=request.session['a_email'])
        return render(request,"adminpanel/index.html",{'uid':uid})
    try:
        email=request.POST['email']
        password=request.POST['password']
        uid=Product_Manager.objects.get(email=email)
        if uid:
            if uid.password==password:
                request.session['a_username']=uid.name
                request.session['a_email']=email
                return render(request,"adminpanel/index.html",{'uid':uid})
            else:
                e_msg="Invalid password"
                return render(request,"adminpanel/sign-in.html",{'e_msg':e_msg})
        else:
            e_msg="Invalid value"
            return render(request,"adminpanel/sign-in.html",{'e_msg':e_msg})
    except:
        e_msg="User Does not exist"
        return render(request,"adminpanel/sign-in.html",{'e_msg':e_msg})
        
def alogout(request):
    if "a_email" in request.session:
        del request.session['a_email']
        del request.session['a_username']
        return render(request,"adminpanel/sign-in.html")
    else:
        return render(request,"adminpanel/sign-in.html")

def doctor_add_page(request):
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    return render(request,"adminpanel/doctor_add.html",{'uid':uid})

def doctor_add(request):
    try:
        uid=Product_Manager.objects.get(email=request.session['a_email'])
        name=request.POST['name']
        speciality=request.POST['speciality']
        contact=request.POST['contact']
        docpic=request.FILES['docpic']
        email=request.POST['email']
        about=request.POST['about']
        doc=Doctor.objects.create(name=name,speciality=speciality,contact=contact,profile_pic=docpic,email=email,about=about)
        data=Doctor.objects.all()
        return render(request,"adminpanel/doctor_list.html",{'data':data,'uid':uid})
    except:
        return render(request,"adminpanel/index.html")

def doctor_view(request):
    data=Doctor.objects.all()
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    return render(request,"adminpanel/doctor_list.html",{'data':data,'uid':uid})
    
def video_add_page(request):
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    return render(request,"adminpanel/yoga_add.html",{'uid':uid})
    
def video_add(request):
    video=request.FILES['video']
    vid=yogavideo.objects.create(videofile=video)
    data=yogavideo.objects.all()
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    return render(request,"adminpanel/video_list.html",{'data':data,'uid':uid})

def video_display(request):
    data=yogavideo.objects.all()
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    return render(request,"adminpanel/video_list.html",{'data':data,'uid':uid})

def category_add_page(request):
    email=request.session['a_email']
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    
    return render(request,"adminpanel/categories_add.html",{'uid':uid})

def category_add(request):
    name=request.POST['name']
    description=request.POST['description']
    cid=Category.objects.create(catname=name,catdiscription=description)
    data=Category.objects.all()
    return render(request,"adminpanel/category_list.html",{'data':data})

def category_list(request):
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    data=Category.objects.all()
    return render(request,"adminpanel/category_list.html",{'data':data,'uid':uid})

def product_add_page(request):
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    cid=Category.objects.all()
    for i in cid:
        print("------------>",i)
    return render(request,"adminpanel/product_add_page.html",{'cid':cid,'uid':uid})




def product_add(request):
    cid=request.POST['cat']
    name=request.POST['name']
    price=request.POST['price']
    quantity=request.POST['quantity']
    productpic=request.FILES['productpic']
    expiredate=request.POST['expiredate']
    description=request.POST['description']
    print("------------------->category",name)
    c_id=Category.objects.get(id=cid)
    pid=product.objects.create(c_id=c_id,pname=name,pdesc=description,pquantity=quantity,pprice=price,pexpiredate=expiredate,profile_pic=productpic)
    if pid:
        print("product add : ")
    data=product.objects.all()
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    return render(request,"adminpanel/product_display.html",{'data':data,'uid':uid})

def product_list(request):
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    data=product.objects.all()
    return render(request,"adminpanel/product_display.html",{'data':data,'uid':uid})

def remove_product(request,pk):
    pid=product.objects.get(id=pk)
    pid.delete()
    data=product.objects.all()
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    return render(request,"adminpanel/product_display.html",{'data':data,'uid':uid})

def profile_page(request):
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    return render(request,"adminpanel/profile_page.html",{'uid':uid})

def admin_update_profile(request):
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    if "companylogo" in request.POST:
        username=request.POST['username']
        password=request.POST['password']
        brandname=request.POST['brandname']
        companylogo=request.POST['companylogo']
        contactno=request.POST['contactno']
        websiteaddress=request.POST['websiteaddress']
        uid.name=username
        uid.password=password
        uid.companylogo=companylogo
        uid.contactno=contactno
        uid.websiteaddress=websiteaddress
        uid.save()
    else:
        username=request.POST['username']
        password=request.POST['password']
        brandname=request.POST['brandname']
        contactno=request.POST['contactno']
        websiteaddress=request.POST['websiteaddress']
        uid.name=username
        uid.password=password
        uid.contactno=contactno
        uid.websiteaddress=websiteaddress
        uid.save()
    return render(request,"adminpanel/index.html",{'uid':uid})

def view_feedback(request):
    data=Feedback.objects.all()
    uid=Product_Manager.objects.get(email=request.session['a_email'])
    return render(request,"adminpanel/feedback.html",{'data':data,'uid':uid})