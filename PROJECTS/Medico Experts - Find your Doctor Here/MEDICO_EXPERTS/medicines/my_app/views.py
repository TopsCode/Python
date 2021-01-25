from django.shortcuts import render
from .models import *
from random import *
from django.core.mail import send_mail
from .utils import *
import re


# Create your views here.
def index(request):
    data=tbl_Medicine.objects.all()
    return render (request,'my_app/index.html',{'data':data})
    

def loginpage(request):
    return render(request,'my_app/main_login.html')

def medicines(request):
    return render(request,'my_app/medicines.html')

def doctor(request):
    return render(request,'my_app/doctor.html')

def contactus(request):
    return render(request,'my_app/contactus.html')

def aboutus(request):
    return render(request,'my_app/aboutus.html')

def registerpage(request):
    return render(request,'my_app/doctor_register.html')

def registerpatient(request):
    return render(request,'my_app/patient_registration.html')

def register_user(request):
    role=request.POST['role']
    print("-------------> role",role)
    try:
        if role=="doctor":
            email=request.POST['email']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            password=request.POST['password']
            cnfpassword=request.POST['cnfpassword']
            gender=request.POST['gender']
            mobile=request.POST['phone']

            passcheck=bool(re.search(r'[A-z][a-z]*',password))

            if passcheck:
                print("--------------->",email)
                print("--------------->",firstname)
                print("--------------->",lastname)
                print("--------------->",password)
                print("--------------->",cnfpassword)
                print("--------------->",gender)
                print("--------------->",mobile)

                #user_check=User.objects.get(email=email)

                # if user_check:
                #      msg="already exist"
                #      return render(request,'my_app/doctor_register.html',{'msg':msg})
                # else:
                if password==cnfpassword:
                    uid=User.objects.create(email=email,password=password,role=role)
                    d_id=Doctor.objects.create(user_id=uid,firstname=firstname,lastname=lastname,gender=gender,mobile=mobile)
                    subject="confermation mail"
                    print("====================================>email")
                    send_mail(subject,"welcome to Medico-Experts","info.medicoexperts007@gmail.com",[email])
                    msg="Registration successfully"
                    return render(request,'my_app/doctor_register.html',{'msg':msg},{'email':email})
                else:
                    msg="password does not match "
                    return render(request,'my_app/doctor_register.html',{'msg':msg})
            else:
                msg="password must contain characters and digit"
                return render(request,'my_app/doctor_register.html',{'msg':msg})
                    

        else:
            role='patient'
            email=request.POST['email']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            password=request.POST['password']
            cnfpassword=request.POST['cnfpassword']
            gender=request.POST['gender']
            birthdate=request.POST['birthdate']
            print("--------------->",email)
            print("--------------->",firstname)
            print("--------------->",lastname)
            print("--------------->",password)
            print("--------------->",cnfpassword)
            print("--------------->",gender)
            print("--------------->",birthdate)
            passcheck=bool(re.search(r'[A-z][a-z]*',password))

            if passcheck:
            #  ucheck=User.objects.get(email=email)
                if password==cnfpassword:
                    uid=User.objects.create(email=email,password=password,role=role)
                    print("---------------->role",role)
                    print("---------------->email",email)
                    print("---------------->password",password)
                        
                    p_id=Patient.objects.create(user_id=uid,firstname=firstname,lastname=lastname,gender=gender,birthdate=birthdate)
                    subject="confermation mail"
                    send_mail(subject,"welcome to Medico-Experts","info.medicoexperts007@gmail.com",[email])
                        
                    msg="Registration successfully"
                    return render(request,'my_app/patient_registration.html',{'msg':msg})
                else:
                    msg="password does not match "
                    return render(request,'my_app/patient_registration.html',{'msg':msg})  
            else:
                msg="password must contain characters and digit"
                return render(request,'my_app/doctor_register.html',{'msg':msg})
            
    except:
       msg="Field Require"
       return render(request,'my_app/patient_registration',{'msg':msg})

def login(request):
    return render(request,'my_app/main_login.html')

# def register(request):
#     return render(request,'my_app/patient_registration.html')

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        del request.session['firstname']
        del request.session['lastname']
        del request.session['pid']
        return render(request,'my_app/index.html')
    else:
        return render(request,'my_app/index.html')

    return render(request,'my_app/patient_registration.html')

# def registerpatient(request):
#     return render(request,'my_app/patient_registration.html')       

def forgotpage(request):
    return render (request,'my_app/forgotpage.html')

def login_evalute(request):

    if request.POST['role'] == 'doctor':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        print(user)

        if user[0]:
            if user[0].password == password and user[0].role == 'doctor':
                
                doctor = Doctor.objects.filter(user_id=user[0])
                did=Doctor.objects.get(user_id=user[0])
                print("------------------------",did)
                request.session['email'] = user[0].email
                request.session['firstname'] = doctor[0].firstname
                request.session['lastname'] = doctor[0].lastname
                
                request.session['role'] = user[0].role
                request.session['id'] = user[0].id

               # request.session['profile_pic']=doctor[0].profile_pic
               # print("----------> Profile pic-->", doctor[0].profile_pic.url)
                return render(request, "doctorapp/dashboard/index.html",{'did':did})
            else:
                msg = "Your password is incorrect or user doesn't exist"
                return render(request, "my_app/main_login.html", {'msg': msg},{'user' : user})
       
    if request.POST['role'] == "patient":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        print(user)

        if user[0]:
            if user[0].password == password and user[0].role == 'patient':
                
                patient = Patient.objects.filter(user_id=user[0])
                pid=Patient.objects.get(user_id=user[0])
                request.session['email'] = user[0].email
                request.session['firstname'] = patient[0].firstname
                request.session['lastname'] = patient[0].lastname
                request.session['pid']=patient[0].id
                request.session['role'] = user[0].role
                request.session['id'] = user[0].id

               # request.session['profile_pic']=doctor[0].profile_pic
               # print("----------> Profile pic-->", doctor[0].profile_pic.url)
                
                return render(request, "doctorapp/patient/pindex.html",{'pid':pid})
            else:
                msg = "Your password is incorrect or user doesn't exist"
                return render(request, "my_app/main_login.html", {'msg': msg}, {'user':user})

      
def profile(request):
    return render(request,"my_app/profile.html")
   
def send_otp(request):
    email=request.POST['email']
    uid=User.objects.get(email=email)
    if uid:
        otp=randint(1111,9999)
        uid.otp=otp
        uid.save()  #update
        subject="OTP Verification"
        print("=======================",otp)
        sendmail(subject,"mail_templates",email,{'otp':otp})
        return render(request,"my_app/reset_password.html",{'email':email})
    else:
        return render(request,"my_app/reset_password.html")

def resetpassword(request):
    email=request.POST['email']
    otp=request.POST['otp']
    password=request.POST['password']
    uid=User.objects.get(email=email)
    if uid:
        if uid.email==email and str(uid.otp)==otp:
            print("-------------->",uid.otp)
            uid.password=password
            uid.save()
            return render(request,'my_app/main_login.html')
        else:
            msg="invalid otp"
            return render (request,'my_app/reset_password.html',{'msg':msg})
    else:
        return render (request,'my_app/reset_password.html')


def all_medicines(request):
    data=tbl_Medicine.objects.getall()
    return render (request,'my_app/index.html',{'data':data})


def medicines_desc(request):
    medi_id=request.POST['medicineid']
    print("====================================",medi_id)
    data=tbl_Medicine.objects.get(id=medi_id)
   
    print("===========================",data)
    return render(request,'my_app/medicinesdescription.html',{'obj':data})

def product(request):
    obj=tbl_Medicine.objects.all()
    print("==========================",obj)
    return render(request,'my_app/allmedicines.html',{'obj':obj})

def medicalshops(request):
    return render(request,'my_app/medical.html')


def Adhlist(request):
    data=shop.objects.all()
    return render(request,'my_app/Ahmedad.html',{'data':data} )




def filter(request,name):
    obj=tbl_Medicine.objects.filter(medicine_type=name)
    print("==========================",obj)
    return render(request,'my_app/allmedicines.html',{'obj':obj})
