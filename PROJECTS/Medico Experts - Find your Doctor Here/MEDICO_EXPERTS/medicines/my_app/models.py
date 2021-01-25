from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique= True)
    password = models.CharField(max_length = 20)
    otp = models.IntegerField(default = 459)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    role = models.CharField(max_length = 10)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)

class Doctor(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=300)
    qualification = models.CharField(max_length=100, blank= True)
    speciality = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 10)
    clinic = models.CharField(max_length= 100,blank = True)
    address = models.CharField(max_length= 500, blank= True)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50, blank= True)
    gender = models.CharField(max_length= 10)
    #birthdate = models.DateField(blank=True)
    location = models.CharField(max_length= 30, blank= True)
    about_doc = models.CharField(max_length= 100, blank= True)
    profile_pic=models.FileField(upload_to='my_app/img/',default='images/member1.png')


class Patient(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length = 10,blank=True)
    address = models.CharField(max_length= 500, blank = True)
    city = models.CharField(max_length = 50,blank=True)
    state = models.CharField(max_length = 50, blank = True)
    gender = models.CharField(max_length= 10,blank=True)
    birthdate = models.DateField(blank=True)
    

    #updated patient profile

    blood_group=models.CharField(max_length=10,blank= True)
    blood_presure=models.CharField(max_length=10,blank= True)
    sugar=models.CharField(max_length=10,blank= True)
    Haemoglobin=models.CharField(max_length=10,blank= True)
    profile_pic=models.FileField(upload_to='my_app/img/',default='images/mehul.png')

class tbl_Medicalshop(models.Model):
    medicalshop_name = models.CharField(max_length=100)
    medicalshop_address = models.CharField(max_length=100)
    medicalshop_phoneno = models.CharField(max_length=100)
    medicalshop_cert = models.FileField(upload_to='my_app/img/',default='patient_icon.png')


class tbl_Medicine(models.Model):
    medicalshop_id = models.ForeignKey(tbl_Medicalshop, on_delete = models.CASCADE)
    medicine_type=models.CharField(max_length=100,default="hhhhh")
    medicines_pic = models.FileField(upload_to='my_app/img/',default='patient_icon.png')
    medicine_name = models.CharField(max_length=100)
    medicine_price = models.CharField(max_length=100)
    medicine_description = models.CharField(max_length=1000)
    medicine_usage = models.CharField(max_length=1000)
    medicine_benefits = models.CharField(max_length=1000)
    medicine_sideeffects = models.CharField(max_length=1000)
    medicine_doc = models.CharField(max_length=1000)



class availability(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    avail_date = models.DateField()
    start_time = models.CharField(max_length = 100)
    status = models.BooleanField(default= False)
    
class Appointment(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    availability_id = models.ForeignKey(availability, on_delete = models.CASCADE,default = None)
    appointment_status = models.BooleanField(default = False)
    payment_status = models.BooleanField(default = False)

class chat(models.Model):
    sender_email=models.EmailField(max_length=40)
    receiver_email=models.EmailField(max_length=40)
    s_message=models.CharField(max_length=500,blank=True)
    r_message=models.CharField(max_length=500,blank=True)
    time=models.CharField(max_length=50,blank=True)




class shop(models.Model):
    s_name=models.CharField(max_length=500)
    s_area=models.CharField(max_length=500,blank=True)
    s_contact=models.CharField(max_length=15,blank=True)
    s_city=models.CharField(max_length=20,blank=True)


