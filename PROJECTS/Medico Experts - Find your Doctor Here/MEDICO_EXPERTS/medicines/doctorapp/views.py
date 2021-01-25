from django.shortcuts import render
from my_app.models import *
from django.core.mail import send_mail
from datetime import datetime, timedelta, date
from my_app.models import chat

# Create your views here.

def index1(request):
    email=request.session['email']
    user = User.objects.filter(email=email)
    print(user)

    if user[0]:   
            did=Doctor.objects.get(user_id=user[0])
            print('-------------------',did)
            print('----------->',did.firstname)
            print('----------->',did.profile_pic.url)
            return render(request,'doctorapp/dashboard/index.html',{'did':did})

def view_patients(request):
    return render(request,'doctorapp/viewpatients.html')

def doctor_profile(request):
    email=request.session['email']
    user = User.objects.filter(email=email)
    print(user)

    if user[0]:   
           
            did=Doctor.objects.get(user_id=user[0])
            print('-------------------',did)
            return render(request,'doctorapp/doctor/dprofile.html',{'did':did})

def patient_profile(request):
    email=request.session['email']
    user = User.objects.filter(email=email)
    print(user)

    if user[0]:   
           
            pid=Patient.objects.get(user_id=user[0])
            print('-------------------',pid)
  
    return render(request,'doctorapp/patient/pindex.html',{'pid':pid})


def update_profile(request):
    email= request.POST['email']
    description=request.POST['about']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    city=request.POST['city']
    state=request.POST['state']
    qualification=request.POST['qlf']
    speciality=request.POST['spec']
    clinic_name=request.POST['clinic']
    address=request.POST['address']
    mobile=request.POST['phone']
    gender=request.POST['gender']
    pic=request.FILES['pic']
    
    
    
    #user=User.objects.get()
    uid=User.objects.get(email=email)
    did=Doctor.objects.get(user_id=uid)
    if did:
        did.firstname=firstname
        did.lastname=lastname
        did.city=city
        did.qualification=qualification
        did.speciality=speciality
        did.clinic=clinic_name
        did.mobile=mobile
        did.address=address
        did.gender=gender
        did.state=state
        did.about_doc=description
        did.profile_pic=pic
        did.save() #update
        msg="profile update successfully"
        print("--------------------------msg",msg)
        return render(request,'doctorapp/doctor/profile1.html',{'msg':msg,'did':did})
    else:
        return render(request,'doctorapp/doctor/profile1.html')

def pupdate_profile(request):
    email= request.POST['email']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    city=request.POST['city']
    state=request.POST['state']
    bdate=request.POST['bdate']
    address=request.POST['address']
    mobile=request.POST['phone']
    gender=request.POST['gender']
    print("=================>",bdate)

    if "pic1" in request.FILES:
        pic=request.FILES['pic1']    
        uid=User.objects.get(email=email)
        pid=Patient.objects.get(user_id=uid)
        if pid:
            pid.firstname=firstname
            pid.lastname=lastname
            pid.city=city
            pid.address=address
            pid.gender=gender
            pid.state=state
            pid.birthdate=bdate
            pid.mobile=mobile
            pid.profile_pic=pic
            pid.save() #update
            msg="profile update successfully"
            print("--------------------------msg",msg)
            return render(request,'doctorapp/patient/pindex.html',{'msg':msg,'pid':pid})
        else:
            return render(request,'doctorapp/patient/pindex.html')

    else:
        #user=User.objects.get()
        uid=User.objects.get(email=email)
        pid=Patient.objects.get(user_id=uid)
        if pid:
            pid.firstname=firstname
            pid.lastname=lastname
            pid.city=city
            pid.address=address
            pid.gender=gender
            pid.state=state
            pid.birthdate=bdate
            pid.mobile=mobile
            pid.save() #update
            msg="profile update successfully"
            print("--------------------------msg",msg)
            return render(request,'doctorapp/patient/pindex.html',{'msg':msg,'pid':pid})
        else:
            return render(request,'doctorapp/patient/pindex.html')




def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request,'my_app/index.html')
    else:
        return render(request,'doctorapp/dashboard/index.html')

def all_doc(request):
    email=request.session['email']
    user = User.objects.filter(email=email)
    print(user)

    if user[0]:   
           
            pid=Patient.objects.get(user_id=user[0])
            print('-------------------',pid)
  
    getall=Doctor.objects.all()
    return render(request,'doctorapp/patient/alldocors.html',{'getall':getall,'pid':pid}) 

def appointment(request):
    doc_email=request.POST['doctorid']
    date=request.POST['avail_date']
    time=request.POST['time']
    avl_id=request.POST['avail_id']
    email=request.session['email']
    print("---------------------------------------------->",avl_id)
    print('-------------------',doc_email)
    print('-------------------',date)
    print('-------------------',time)
    print('-------------------',avl_id)
    user = User.objects.filter(email=email)
    print(user)
    if user[0]:   
           
            pid=Patient.objects.get(user_id=user[0])
            
            
            print('-------------------',pid)


            context={
                "doc_email":doc_email,
                "date":date,
                "time":time ,
                "avl_id":avl_id ,
            }


           
            return render(request,'doctorapp/patient/appobook.html',{'pid':pid ,'context':context})
    
    return render(request,'doctorapp/patient/appobook.html',{'pid':pid , 'context':context})
    

def appo_data(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    dob=request.POST['dob']
    gender=request.POST['gender']
    email=request.POST['email']
    mobile=request.POST['mobile']
    return render(request,'doctorapp/patient/appointment.html')
    
def pprofile(request):
    return render(request,'doctorapp/patient/p_profile.html')

"""
def mark_availability(request):
    if request.session['role']=="Doctor":
        doctor_id=Doctor.objects.get(user_id=request.session['id'])
        print("------------->",doctor_id)
        try:
            all_avail=availability.objects.get(doctor_id=doctor_id)
            if all_avail:
                return render(request,'doctorapp/appointment/mark_availability.html',{'all_avail':all_avail})
            else:
                return render(request,'doctorapp/appointment/mark_availability.html')
        except:
            return render(request,'doctorapp/dashboard/index.html')

    else:
        return render(request,'doctorapp/dashboard/index.html')
"""

def mark_availability(request):
    email=request.session['email']
    user = User.objects.filter(email=email)
    print(user)

    if user[0]:   
        did=Doctor.objects.get(user_id=user[0])
        print('-------------------',did)
    
    return render(request,'doctorapp/appointment/mark_availability.html',{'did':did})

def store_all_availabilities(request):
    if request.session['role'] == 'doctor':
        start_date = datetime.strptime(request.POST['start_date'], "%Y-%m-%d").date()
        end_date = datetime.strptime(request.POST['end_date'], "%Y-%m-%d").date()
        
        start_time = request.POST['start_time']
        print('this is date', start_date)
        end_time = request.POST['end_time']
        doctor_id = Doctor.objects.get(user_id=request.session['id'])
        
        current_time = date.today()
        
        print(type(current_time))
        print(type(start_date))
        # if start_date > current_time and end_time > current_time:
        
        difference_in_days = end_date - start_date
        for i in range(0, int(difference_in_days.days)+1):
            modified_date = start_date + timedelta(days=i)
            for j in range(int(start_time), int(end_time) + 1):
                availability.objects.create(doctor_id=doctor_id, avail_date=modified_date, start_time=str(j)+':00')
                availability.objects.create(doctor_id=doctor_id, avail_date=modified_date, start_time=str(j)+':30')
        all_availabilities = availability.objects.filter(doctor_id=doctor_id)

        print("--------------->",start_date)
        print("--------------->",start_time)
        print("--------------->",end_date)
        print("--------------->",end_time)
        for all in all_availabilities:
            print("----------->",all)
        
        return render(request,"doctorapp/appointment/mark_availability.html")
        # else:
        #     all_availabilities = availability.objects.filter(doctor_id = doctor_id)
        #     return render(request, "doctorfinder/mark_availability.html", {'all_availabilities': all_availabilities,'error':'Start and end time should be greater than current date'})
    else:
        return render(request,"doctorapp/dashboard/index.html")

def viewavalability(request,pk=None):
    email=request.session['email']
    user = User.objects.filter(email=email)
    print(user)

    print("======================> pk",pk)
    if user[0]:   
            pid=Patient.objects.get(user_id=user[0])
            print('-------------------',pid)
            did=Doctor.objects.all()   
            doctor=Doctor.objects.get(id=pk)
            a_id=availability.objects.filter(doctor_id=doctor)
            print("availability------------------------>",a_id)

            for i in a_id:
                print(i.avail_date)

            print("Doctor ----------------------------> ",doctor.firstname)

            return render(request,"doctorapp/patient/viewavalability.html",{'pid':pid ,'did':did,'doctor':doctor,'a_id':a_id} )
    return render(request,"doctorapp/patient/viewavalability.html",{'pid':pid , 'did':did})


def Book_appo(request):
    abcid=request.session['id']
    avl_id = request.POST['avl_id']
    patient_id = request.POST['patient_id']
    doc_id = request.POST['doctor_id']
    print("--------------------------------------------->",abcid)
    print("--------------------------------------------->",avl_id)
    print("--------------------------------------------->",patient_id)
    pid=Patient.objects.get(id=request.session['pid'])
    uid=User.objects.get(id=abcid)
    print("--------------------------------------------->",pid)
    avl_id=availability.objects.get(id=avl_id)
    print("================================",doc_id)
    appo_id=Appointment.objects.create(doctor_id=doc_id,patient_id=pid,user_id=uid,availability_id=avl_id)
    print("==============================================",appo_id)
    return render(request,"doctorapp/patient/viewavalability.html" )


def all_appo(request):
    email=request.session['email']
    user = User.objects.filter(email=email)
    print(user)

    if user[0]:   
        did=Doctor.objects.get(user_id=user[0])
        print('-------------------',did)
   
    abc=request.session['id']
    print("-------------------------------",abc)
    did=Doctor.objects.get(user_id=abc)
    print("-------------------------------",did)

    data=Appointment.objects.filter(doctor_id=did).select_related('patient_id','user_id','availability_id')
    for i in data:
        print("-------------->",i.patient_id.firstname)
        print("-------------->",i.availability_id.avail_date)
        print("---------------------->",i.user_id.email)
    
    print("----------================",data)
    return render(request,"doctorapp/doctor/all_appointments.html",{'data':data,'did':did})


def send_mail2(request):
    email=request.POST['email']
    avi_id=request.POST['avl_id']
    schedule = availability.objects.get(id=avi_id)
    schedule.status = True
    schedule.save() 
    subject="Appointment Confirmation  mail"
    send_mail(subject,"Your appointment has been suceesfully booked ","info.medicoexperts007@gmail.com",[email])
    return render(request,'doctorapp/dashboard/index.html')

def chatvalue(request):
    data=Doctor.objects.all()
    print("================>>>>>>>>>>data",data)
    return render(request,'doctorapp/patient/chat.html',{'data':data})

def chatbot(request,pk=None):
    email=request.session['email']
    user = User.objects.filter(email=email)
    print(user)

    if user[0]:   
            pid=Patient.objects.get(user_id=user[0])
            print('-------------------',pid)
    print("------------------>",pk)
    #did=Doctor.objects.get(firstname=pk)
    #print("------------------>",did.user_id)
    chatdata=chat.objects.all()
    uid=User.objects.get(email=pk)
    did=Doctor.objects.get(user_id=uid)
    data=Doctor.objects.all()
    print("======================>>",did)
    print("======================>>",did)
   
    return render(request,"doctorapp/patient/chat.html",{'pid':pid,'uid':uid,'data':data,'did':did,'chatdata':chatdata})

def sendmessage(request):
    role=request.POST['role']
    s_email=request.POST['s_email']
    r_email=request.POST['r_email']
    message=request.POST['message']
    
    if role=="doctor":
        cid=chat.objects.create(sender_email=s_email,receiver_email=r_email,s_message=message)
    if role=="patient":
        cid=chat.objects.create(sender_email=s_email,receiver_email=r_email,r_message=message)
    
    chatdata=chat.objects.all()
    data=Doctor.objects.all()
    uid=User.objects.get(email=s_email)

    did=Doctor.objects.get(user_id=uid)
    return render(request,"doctorapp/patient/chat.html",{'uid':uid,'data':data,'did':did,'chatdata':chatdata})


def dsendmessage(request,pk=None):
    role=request.POST['role']
    s_email=request.POST['s_email']
    r_email=request.POST['r_email']
    message=request.POST['message']
    
    if role=="patient":
        cid=chat.objects.create(sender_email=s_email,receiver_email=r_email,s_message=message)
    if role=="doctor":
        cid=chat.objects.create(sender_email=s_email,receiver_email=r_email,r_message=message)
    
    chatdata=chat.objects.all()
    data=Patient.objects.all()
    uid=User.objects.get(email=s_email)

    did=Doctor.objects.get(user_id=uid)
    return render(request,"doctorapp/doctor/dchat.html",{'uid':uid,'data':data,'did':did,'chatdata':chatdata})

def dchatbot(request,pk=None):
    email=request.session['email']
    user = User.objects.filter(email=email)
    print(user)

    if user[0]:   
            did=Doctor.objects.get(user_id=user[0])
            print('-------------------',did)
    print("------------------>",pk)
    #did=Doctor.objects.get(firstname=pk)
    #print("------------------>",did.user_id)
    chatdata=chat.objects.all()
    uid=User.objects.get(email=pk)
    pid=Patient.objects.get(user_id=uid)
    data=Patient.objects.all()
    print("======================>>",pid)
    print("======================>>",pid)
   
    return render(request,"doctorapp/doctor/dchat.html",{'pid':pid,'uid':uid,'data':data,'did':did,'chatdata':chatdata})
    
def dchat(request):
    data=Patient.objects.all()
    print("================>>>>>>>>>>data",data)
    return render(request,'doctorapp/doctor/dchat.html',{'data':data})
