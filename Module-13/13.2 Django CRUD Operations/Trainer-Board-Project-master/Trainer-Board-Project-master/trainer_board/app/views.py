from django.shortcuts import render
from .models import * 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail


# Create your views here.


def home(request):
    return render(request,"app/dashboard.html")

def loginpage(request):
    return render(request,"app/login.html")

def registerpage(request):
    return render(request,"app/register.html")

def registeruser(request):
    obj=user()
    obj.name=request.POST['name']
    obj.email=request.POST['email']
    obj.password=request.POST['password']
    enter=user.objects.create(name= obj.name,email=obj.email,password=obj.password)
    return render(request,"app/login.html")

def login_check(request):
    try:
        email=request.POST['email']     
        password=request.POST['password']
        u_data=user.objects.get(email=email)
        if u_data:
            if u_data.email==email and u_data.password==password:
                getall=task.objects.all()
                request.session['name']=u_data.name
                request.session['id']=u_data.id
                
                return render(request,"app/dashboard.html",{'getall':getall,'u_data':u_data})
            else:
                return render(request,"app/login.html")      
        else:
           return render(request,"app/login.html")
    except user.DoesNotExist:
        return render(request,"app/login.html")

def post_task(request):
    obj=task()
    obj.user_id=request.session['name']
    obj.desc=request.POST['desc']
    obj.status=request.POST['addworkstatus']
    #obj.user_id=user.objects.get(id=request.session['id'])
    post_task_data=task.objects.create(user_id=obj.user_id,desc=obj.desc,status=obj.status)
    getall=task.objects.all()
    return render(request,"app/dashboard.html",{'getall':getall})

def user_dash(request):
    return request(request,"app/dashboard.html")

def userdashboard(request):
    name=request.session['name']
    obj_info =task.objects.filter(user_id=name)
    #user=task.objects.get(user_id=request.session['id'])
    return render(request,"app/userdashboard.html",{'obj_info':obj_info})

#def edit_task(request,pk=None):
 #   if pk:
  #      objdata=task.objects.get(id=pk)
#    return render(request,'app/myfile.html',{'objdata':objdata})

def edit_task(request):
    if 'btnupdate' in request.POST:
        id=request.POST['idkey']
        obj =task.objects.get(id=id)
        obj.desc=request.POST['desc']
        obj.status=request.POST['workstatus']
        e_subject="Trainer Board Task updated "
        name=obj.user_id
        mydata=user.objects.get(name=name)
        if mydata:
            email=mydata.email
            request.session[email]=email
            msg="Hello "+request.session['name']+" your task is updated successfully !!"
            send_mail(e_subject,msg,"anjali.20.learn@gmail.com",[email])
            obj.save()
            getall=task.objects.all()
            return render(request,'app/dashboard.html',{'getall':getall})
    #elif 'btndelete' in request.POST:
     #   id=request.POST['idkey']
      #  delete_row = task.objects.get(id=id)
       # delete_row.delete()
        #getall=task.objects.all()
        #return render(request,'app/dashboard.html',{'getall':getall})


def delete_task(request):
        id=request.POST['delkey']
        delete_row = task.objects.get(id=id)
        
        name=delete_row.user_id
        mydata=user.objects.get(name=name)
        if mydata:
            email=mydata.email
            e_subject="Trainer Board Task updated "
            msg="Hello "+request.session['name']+" your task is deleted successfully !!"
            send_mail(e_subject,msg,"anjali.20.learn@gmail.com",[email])
            delete_row.delete()
            getall=task.objects.all()
            return render(request,'app/dashboard.html',{'getall':getall})