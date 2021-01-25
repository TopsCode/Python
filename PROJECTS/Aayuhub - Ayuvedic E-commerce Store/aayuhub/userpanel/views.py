from django.shortcuts import render
from adminpanel.models import *
from random import *
from .utils import *
from django.core.mail import send_mail
#from vseller.models import product

# Create your views here.
def index_page(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        data=product.objects.all()
        call=Category.objects.all()
        if uid:
            count=addToCart.objects.filter(uid=uid).count()
            return render(request, "userpanel/index.html",{'uid':uid,'data':data,'count':count,'call':call})
        else: 
            e_msg="invalid input"
            return render(request, "userpanel/login.html",{'e_msg':e_msg})
    else:
        data=product.objects.all()
        call=Category.objects.all()
        return render(request, "userpanel/index.html",{'data':data,'call':call})

def login_page(request):
    return render(request, "userpanel/login.html")

def gallery(request):
    if "email" in request.session:
            uid=User.objects.get(email=request.session['email'])
            data=product.objects.all()
            return render(request, "userpanel/gallery.html",{'uid':uid,'data':data})
    else:
        data=product.objects.all()
        return render(request, "userpanel/gallery.html",{'data':data})

def doctor_details(request):
    if "email" in request.session:
            uid=User.objects.get(email=request.session['email'])
            data=Doctor.objects.all()
            return render(request,"userpanel/doctor_details.html",{'uid':uid,'data':data})
    else:
        data=Doctor.objects.all()
        return render(request,"userpanel/doctor_details.html",{'data':data})

def registration_page(request):
    data=Area.objects.all()
    return render(request, "userpanel/reg.html",{'data':data})

def resistration_user(request):
    try:
        area=request.POST['area']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        address=request.POST['address']
        contact=request.POST['contact']
        pic=request.FILES['pic']
        print("----------->",area)
        print("----------->",firstname)
        print("----------->",lastname)
        print("----------->",email)
        print("----------->",address)
        print("----------->",contact)
        print("----------->",pic)
        aid=Area.objects.get(id=area)   
        uid=User.objects.create(area_id=aid,firstname=firstname,lastname=lastname,email=email,password=password,address=address,contact=contact,profile_pic=pic)
        if uid:
            s_msg="successfully resistration !!"
            send_mail("confirmation mail","welcome to Ayuhub","aayuhub@gmail.com",[email])
        
            return render(request, "userpanel/login.html",{'s_msg':s_msg}) 
        else:
            return render(request, "userpanel/resistration.html")
    except:
        e_msg="invalid input"
        return render(request, "userpanel/resistration.html",{'e_msg':e_msg})

def login_user(request):
    try:
        email=request.POST['email']
        password=request.POST['password']
        uid=User.objects.get(email=email)
     
        if uid:
            if uid.password==password:
                request.session['firstname']=uid.firstname
                request.session['email']=uid.email
                request.session['id']=uid.id
                data=product.objects.all()
                return render(request, "userpanel/index.html",{'uid':uid,'data':data})
            else:   
                e_msg="password does not match"
                return render(request, "userpanel/login.html",{'e_msg':e_msg})
        else: 
            e_msg="invalid input"
            return render(request, "userpanel/login.html",{'e_msg':e_msg})
    except:
        e_msg="user does not exist"
        return render(request, "userpanel/login.html",{'e_msg':e_msg})


def logout_page(request):
    if "email" in request.session:
        del request.session['firstname']
        del request.session['email']
        del request.session['id']
        s_msg="sign-out successfully "
        return render(request, "userpanel/login.html",{'s_msg':s_msg})  
    else:
        return render(request, "userpanel/login.html") 


def forgot_password(request):
    return render(request, "userpanel/forgot_password.html")


def send_otp(request):
    
        email=request.POST['email']
        print("-------------->email",email)
        uid=User.objects.get(email=email)

        if uid:
            otp=randint(1111,9999)
            uid.otp=otp
            uid.save()
            print("---------------> otp",otp)
            send_mail("forgot password","Otp is: "+str(otp),"aayuhub@gmail.com",[email])
            return render(request, "userpanel/reset-pass.html",{'email':email})
        else:
            return render(request, "userpanel/forgot_password.html")
    
def reset_password(request):
    try:
        email=request.POST['email']
        otp=request.POST['otp']
        newpassword=request.POST['newpassword']
        retypepassword=request.POST['retypepassword']

        uid=User.objects.get(email=email)

        if uid:
            if str(uid.otp)==str(otp) and newpassword==retypepassword:
                uid.password=newpassword
                uid.save()
                s_msg="successfully reset password"
                return render(request, "userpanel/login.html",{'s_msg':s_msg})
            else:
                e_msg="password or otp does not match"
                return render(request, "userpanel/reset-pass.html",{'e_msg':e_msg})
        else:            
            return render(request, "userpanel/reset-pass.html")
    except:
        e_msg="user does not exist"
        return render(request, "userpanel/reset-pass.html",{'e_msg':e_msg})


def profile(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request, "userpanel/profile.html",{'uid':uid})


def feedback_page(request):
    data=Review_user.objects.all().prefetch_related('uid')
    try:
        
        email=request.POST['email']
        feedback=request.POST['feedback']
        rating=request.POST['rating']

        uid=User.objects.get(email=request.session['email'])
        
        print(uid)

        if uid:
            f_back=Review_user.objects.create(feedback=feedback,rating=rating,uid=uid)
            
            if f_back:
                send_mail("confirmation mail","feedback:"+feedback,"mahendrasuthar731@gmail.com",[email])
                return render(request, "userpanel/feedback.html",{'data':data})
        else:
            return render(request, "userpanel/feedback.html")
    except:
        return render(request, "userpanel/feedback.html")


def edit_profile(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request, "userpanel/editprofile.html",{'uid':uid})

def update_profile(request):
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    mobile=request.POST['mobile']
    pic=request.FILES['pic']

    uid=User.objects.get(email=request.session['email'])

    if uid:
        uid.username=username
        uid.email=email
        uid.mobile=mobile
        uid.password=password
        uid.profile_pic=pic
        uid.save()
        return render(request, "userpanel/profile.html")
    else:
        return render(request, "userpanel/editprofile.html")

        



def about_page(request):
    return render(request, "userpanel/about.html")

def blog_single(request):
    return render(request, "userpanel/blog-single.html")


def blog(request):
    return render(request, "userpanel/blog.html")


def cart_page(request):
    try:
        if "email" in request.session:
            uid=User.objects.get(email=request.session['email'])
            data=addToCart.objects.filter(uid=uid)
            count=addToCart.objects.filter(uid=uid).count()
            return render(request, "userpanel/cart.html",{'uid':uid,'data':data,'count':count})
            
    except:
        return render(request, "userpanel/cart.html")

def update_cart(request):
    try:

        return render(request, "userpanel/cart.html",{'data':data})
    except:
        return render(request, "userpanel/cart.html")
    

def wish_list(request):
    uid=User.objects.get(email=request.session['email'])
    data=wishlist.objects.filter(uid=uid)
    for i in data:
        print("-------------->",i.uid.firstname)
        print("-------------->",i.pid.pname)
        count=addToCart.objects.filter(uid=uid).count()
    return render(request, "userpanel/wishlist.html",{'uid':uid,'data':data,'count':count})

def wishlist_remove(request,pk=None):
    print("---------->",pk)
    uid=User.objects.get(email=request.session['email'])
    wid=wishlist.objects.get(id=pk)
    wid.delete()
    data=wishlist.objects.filter(uid=uid)
    return render(request, "userpanel/wishlist.html",{'data':data})


def check_out(request):
    return render(request, "userpanel/checkout.html")

def contact_page(request):
    return render(request, "userpanel/checkout.html")


def product_single(request):
    return render(request, "userpanel/product-single.html")


def shop_page(request):
    try:
        #.prefetch_related('uid')
        data=product.objects.all()
        return render(request, "userpanel/shop.html",{'data':data})
    except:
        return render(request, "userpanel/shop.html")

def yoga_video(request):
    uid=User.objects.get(email=request.session['email'])
    #send_mail("HELLO","welcome to Ayuhub","aayuhub@gmail.com",[uid.email])

    data=yogavideo.objects.all()
    return render(request,"userpanel/yoga_videos.html",{'data':data})



def wishlist_add(request,pk=None):
    pid=product.objects.get(id=pk)
    
    uid=User.objects.get(email=request.session['email'])
    
    print("---------> pid ",pid.id)
    print("---------> uid ",uid.id)
    
    user_id=wishlist.objects.filter(uid=uid.id)
    if user_id:
        print("-------------->exist")
        product_id=wishlist.objects.filter(pid=pid.id)
        if product_id:
            print("---------------> update data ")
            qty=product_id[0].qty+1
            price=qty*pid.pprice
            print("------------->qty = ",qty)
            print("------------->price = ",price)
            product_id[0].qty=qty
            product_id[0].price=price
            product_id[0].save()

            data=wishlist.objects.filter(uid=uid)    
            return render(request, "userpanel/wishlist.html",{'data':data})
        else:
            wid=wishlist.objects.create(uid=uid,pid=pid,qty=1,price=pid.pprice)
            data=wishlist.objects.filter(uid=uid)    
            return render(request, "userpanel/wishlist.html",{'data':data})
    else:
        wid=wishlist.objects.create(uid=uid,pid=pid,qty=1,price=pid.pprice)
        data=wishlist.objects.filter(uid=uid)    
        return render(request, "userpanel/wishlist.html",{'data':data})
        print("-------------->user does not exist")

    


"""
def buy_product(request):
    firstname=request.POST['firstname']
    email=request.POST['email']
    lastname=request.POST['lastname']
    mobile=request.POST['mobile']
    address=request.POST['address']
    city=request.POST['city']
    state=request.POST['state']
    code=request.POST['code']

    uid=User.objects.get(email=request.session['email'])
    b_id=Buy_product.objects.create(firstname=firstname,lastname=lastname,mobile=mobile,address=address,city=city,state=state,code=code)

    if b_id:
        uid.firstname=firstname
        uid.email=email
        uid.mobile=mobile
        uid.lastname=lastname
        uid.address=address
        uid.city=city
        uid.state=state
        uid.code=code
        uid.save()
        return render(request, "userpanel/checkout.html")
    else:
        return render(request, "userpanel/checkout.html")
"""

def add_to_cart(request,pk):
    w_id=wishlist.objects.get(id=pk)
    if w_id:
        uid=w_id.uid
        pid=w_id.pid
        qty=w_id.qty
        price=w_id.price
        cid=addToCart.objects.create(uid=uid,pid=pid,qty=qty,price=price)
        if "email" in request.session:
            uid=User.objects.get(email=request.session['email'])
            data=addToCart.objects.filter(uid=uid)
            return render(request, "userpanel/cart.html",{'uid':uid,'data':data})

def addresspage(request,pk):
    if "email" in request.session:
            data=addToCart.objects.filter(id=pk)
            uid=User.objects.get(email=request.session['email'])
            return render(request,"userpanel/address.html",{'uid':uid,'data':data})
    

def remove_product(request,pk):
    data=addToCart.objects.get(id=pk)
    data.delete()
    data=addToCart.objects.filter()
    uid=User.objects.get(email=request.session['email'])
    return render(request, "userpanel/cart.html",{'uid':uid,'data':data})
                   
def placeorder(request):
    uid=User.objects.get(email=request.session['email'])
    cartid=request.POST['cartid']
    address=request.POST['address']
    aid=addToCart.objects.get(id=cartid)
    #useremail=aid.uid.email
    order_id=placeOrder.objects.create(uid=aid.uid,pid=aid.pid,qty=aid.qty,price=aid.price,address=address)

    print("----------->email : ",uid.email)
    subject="order confirmation"
    msg="hello your order confirm successfully "
    print("####---------->",order_id.pid.pname)
    print("####---------->",order_id.qty)
    print("####---------->",order_id.price)
    print("####---------->",order_id.status)
    
    #wid=wishlist.objects.get(id=aid.id)
    #print("===================>",wid.price)
    
    sendmail("order confirmation", 'mailtemplates', uid.email, {'order_id': order_id,'uid':uid})
    #send_mail("Order Confirmation","welcome to Ayuhub","aayuhub@gmail.com",[uid.email])
    
    aid.delete()
    #order_id.delete()
    uid=User.objects.get(email=request.session['email'])
    data=product.objects.all()
    print("product placed",msg)    
    if uid:
        count=addToCart.objects.filter(uid=uid).count()
        print("next to index page ",msg)
        return render(request, "userpanel/index.html",{'uid':uid,'data':data,'count':count})

def add_feedback(request):
    uid=User.objects.get(email=request.session['email'])
    comment=request.POST['comment']
    fid=Feedback.objects.create(uid=uid,comments=comment)
    data=product.objects.all()
    if uid:
        count=addToCart.objects.filter(uid=uid).count()
        return render(request, "userpanel/index.html",{'uid':uid,'data':data,'count':count})

