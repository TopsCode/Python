from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .utils import *
from django.urls import reverse
import random
import stripe

stripe.api_key = "<YOUR STRIPE SECRATE KEY>"

# Create your views here.

def index(request):
    return render(request, "user/index.html")

def getProductsByCategory(name):
    category = Category.objects.get(name = name)
    products = Product.objects.filter(category = category, active = True)

    brands = {}
    subcategories = {}
    colors = ColorVariation.objects.all()
    
    for product in products:
        brand = str(product.productManager)
        category = str(product.category)
        subcategory = str(product.subcategory)
        
        if brand in brands: brands[brand] += 1 
        else: brands[brand] = 1

        if subcategory in subcategories: subcategories[subcategory] += 1
        else: subcategories[subcategory] = 1

    brands = brands.items()
    subcategories = subcategories.items()

    return products, brands, subcategories, colors

def getProductsBySubcategories(products, subcategory_list):
    filteredProducts = []
    for product in products:
        if str(product.subcategory) in subcategory_list:
            filteredProducts.append(product)
    return filteredProducts

def getProductsByBrandName(products, brand_list):
    filteredProducts = []
    for product in products:
        if str(product.productManager) in brand_list:
            filteredProducts.append(product)
    return filteredProducts

def getProductsByColors(products, color_list):
    filteredProducts = []
    for product in products:
        productColorList = product.colorList()
        for color in color_list:
            if color in productColorList and product not in filteredProducts:
                filteredProducts.append(product)
    return filteredProducts

def men(request):
    # RETRIVE PRODUCTS BY CATEGORY "MEN"
    category = "men"
    products, brands, subcategories, colors = getProductsByCategory(category)
    
    return render(request, "user/shop.html", {
        "products": products, 
        "quantity": len(products),
        "category": category,
        "subcategories": subcategories,
        "brands": brands,
        "colors": colors
    })

def women(request):
    # RETRIVE PRODUCTS BY CATEGORY "WOMEN"
    category = "women"
    products, brands, subcategories, colors = getProductsByCategory(category)
    
    return render(request, "user/shop.html", {
        "products": products, 
        "quantity": len(products),
        "category": category,
        "subcategories": subcategories,
        "brands": brands,
        "colors": colors
    })

def accessories(request):
    # RETRIVE PRODUCTS BY CATEGORY "ACCESSORIES"
    category = "accessories"
    products, brands, subcategories, colors = getProductsByCategory(category)
    
    return render(request, "user/shop.html", {
        "products": products, 
        "quantity": len(products),
        "category": category,
        "subcategories": subcategories,
        "brands": brands,
        "colors": colors
    })

def filter(request):
    if request.method == "GET":
        return HttpResponseRedirect("/")

    category = request.POST["category"]
    products, brands, subcategories, colors = getProductsByCategory(category)
    
    # FILTER BY CATEGORY AND PRICE RANGE
    category = Category.objects.get(name = category)
    min_price = request.POST["min_price"]
    max_price = request.POST["max_price"]
    products = Product.objects.filter(category = category, active = True, price__range=(min_price,max_price))

    # ORDER THE PRODUCTS BY PRICE AND DATE
    orderby = request.POST['orderby']
    if orderby == "price":
        products = products.order_by('price')
    elif orderby == "price-desc":
        products = products.order_by('-price')
    elif orderby == "date":
        products = products.order_by('-created_at')
    
    # FILTER BY SUBCATEGORIES
    selected_subcategories = request.POST.getlist("subcategories")
    if selected_subcategories:
        products = getProductsBySubcategories(products, selected_subcategories)
    
    # FILTER BY BRANDS
    selected_brands = request.POST.getlist("brands")
    if selected_brands:
        products = getProductsByBrandName(products, selected_brands)
    
    # FILTER BY COLORS
    selected_colors = request.POST.getlist("colors")
    if selected_colors:
        products = getProductsByColors(products, selected_colors)

    return render(request, "user/shop.html", {
        "products": products, 
        "quantity": len(products),
        "category": category,
        "subcategories": subcategories,
        "brands": brands,
        "colors": colors,
        "selected_subcategories": selected_subcategories,
        "selected_brands": selected_brands,
        "selected_colors": selected_colors,
        "orderby": orderby
    })

def product_single(request, id, title):
    # RETRIVE PRODUCT BY PRODUCT ID
    product = Product.objects.get(id=id, title=title)
    return render(request, "user/product_single.html", {"product": product})

def about(request):
    return render(request, "user/about.html")

def contact(request):
    return render(request, "user/contact.html")

def support(request):
    return render(request, "user/support.html")

def blog(request):
    return render(request, "user/blog.html")

def blog_single(request):
    return render(request, "user/blog_single.html")

def wishlist(request):
    # CHECK IF SESSION IS AVAILABLE
    if "email" not in request.session:
        return HttpResponseRedirect('/login/')

    # RETRIVE WISHLIST ITEMS
    wishlist_data = WishlistData.objects.filter(customer_id = request.session["customer_id"])
    
    request.session["wishlist_length"] = len(wishlist_data)
    #request.session['wishlist_data'] = wishlist_data

    # RETRIVE CART ITEMS
    cart_data = CartData.objects.filter(customer_id = request.session["customer_id"])

    request.session["cart_length"] = len(cart_data)
    #request.session['cart_data'] = cart_data

    return render(request, "user/wishlist.html", {"wishlist_data": wishlist_data})

def cart(request):
    # CHECK IF SESSION IS AVAILABLE
    if "email" not in request.session:
        return HttpResponseRedirect('/login/')

    # RETRIVE WISHLIST ITEMS
    wishlist_data = WishlistData.objects.filter(customer_id = request.session["customer_id"])
    
    request.session["wishlist_length"] = len(wishlist_data)
    #request.session['wishlist_data'] = wishlist_data

    # RETRIVE CART ITEMS
    cart_data = CartData.objects.filter(customer_id = request.session["customer_id"])

    request.session["cart_length"] = len(cart_data)
    #request.session['cart_data'] = cart_data

    # CALCULATE TOTAL AMOUNT
    sub_total = 0
    for cart in cart_data:
        sub_total += cart.total()
    
    return render(request, "user/cart.html", {"cart_data": cart_data, "sub_total": sub_total, "grand_total": sub_total + 18})

def checkout(request):
    # CHECK IF SESSION IS AVAILABLE
    if "email" not in request.session:
        return HttpResponseRedirect('/login/')

    # RETRIVE CART ITEMS
    cart_data = CartData.objects.filter(customer_id = request.session["customer_id"])

    # CHECK IF QUANTITY IS OUT OF STOCK
    for cart_item in cart_data:
        if cart_item.quantity > cart_item.product.stock:
            return HttpResponseRedirect('/cart/')

    # CALCULATE TOTAL AMOUNT
    sub_total = 0
    for cart in cart_data:
        sub_total += cart.total()
    
    # REDIRECT TO CART PAGE IF CART IS EMPTY
    if sub_total == 0:
        return HttpResponseRedirect('/cart/')

    return render(request, "user/checkout.html", {"cart_data": cart_data, "sub_total": sub_total, "grand_total": sub_total + 18})

def order_complete(request):
    return render(request, "user/order_complete.html")



def register (request):
    # CHECK IF SESSION IS AVAILABLE
    if "email" in request.session:
        return HttpResponseRedirect('/')
    return render(request, "user/register.html")

def login (request):
    # CHECK IF SESSION IS AVAILABLE
    if "email" in request.session:
        return HttpResponseRedirect('/')

    # CHECK IF COOKIES ARE AVAILABLE
    elif request.COOKIES.get('email'):
        cookie_data = {
            'email': request.COOKIES.get('email'),
            'password': request.COOKIES.get('password'),
        }
        return render(request, "user/login.html", {"cookie_data": cookie_data})
    
    else:
        return render(request, "user/login.html")

def forget_password(request):
    # CHECK IF SESSION IS AVAILABLE
    if "email" in request.session:
        return HttpResponseRedirect('/')
    return render(request, "user/forget_password.html")

def register_user (request):
    if request.method =="GET":
        return HttpResponseRedirect('/register/')
    
    try:
        # RETRIVE FORM DATA
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        # CREATE A USER IN DATABASE AND THROW AN EXCEPTION IF THE EMAIL ALREADY EXIST
        user = User.objects.create(username = username, email = email, password = password, role = "customer")
        customer = Customer.objects.create(user_id = user.id)

        # CHECK IF USER OBJECT IS CREATED 
        if user:
            # SEND EMAIL
            mail_subject = "Confirmation Mail"
            mail_template = "mail_welcome"
            sendmail(mail_subject, mail_template, email, {"username": username, "email": email})
            success_message = "Registration successful."
            return render(request, "user/login.html", {'success_message' : success_message})
        else:
            error_message = "Registration error. Try again."
            return render(request, "user/register.html", {'error_message' : error_message})
        
    except:
        error_message = "User already have an account."
        return render(request, "user/register.html", {'error_message' : error_message})

def login_user (request):
    if request.method =="GET":
        return HttpResponseRedirect('/login/')
    
    # RETRIVE FORM DATA
    email = request.POST["email"]
    password = request.POST["password"]

    # ACCESS USER FROM THE DATABASE
    user = User.objects.filter(email = email, role = "customer")
    if user and user[0].password == password:
        # ACCESS CUSTOMER FROM DATABASE
        customer = Customer.objects.get(user_id = user[0].id)
        wishlist_data = WishlistData.objects.filter(customer = customer)
        cart_data = CartData.objects.filter(customer = customer)

        # CREATE SESSION
        request.session['username'] = customer.user.username
        request.session['email'] = customer.user.email
        request.session['role'] = customer.user.role
        request.session['customer_id'] = customer.id
        request.session['wishlist_length'] = len(wishlist_data)
        request.session['cart_length'] = len(cart_data)
        #request.session['wishlist_data'] = wishlist_data
        #request.session['cart_data'] = cart_data

        response = HttpResponseRedirect('/')
        
        # SET OR DELETE COOKIES FOR "REMEMBER ME"
        if request.POST.get("checked"):
            max_age = 365*24*60*60
            response.set_cookie('email', email, max_age)
            response.set_cookie('password', password, max_age)
        else:
            response.delete_cookie('email')
            response.delete_cookie('password')
            
        return response
                
    else:
        error_message = "Incorrect email or password."
        return render(request, "user/login.html", {'error_message' : error_message})

def forget_password_user(request):
    if request.method =="GET":
        return HttpResponseRedirect('/forget_password/')
    
    try:
        # RETRIVE FORM DATA
        email = request.POST["email"]

        # ACCESS USER FROM THE DATABASE
        user = User.objects.get(email = email)
                    
        # SEND OTP TO EMAIL
        otp = random.randint(1000,9999)
        user.otp = otp
        user.save()
        mail_subject = "OTP"
        mail_message = str(otp) + " is your OTP to change you password in your FoodBlog."
        send_otp_mail(mail_subject, mail_message, user.email)
        
        success_message = "OTP has been sent to this email address."
        return render( request, "user/forget_password_otp.html", {'success_message' : success_message, "email" : user.email})
    
    except :
        error_message = "Email does not exist."
        return render(request, "user/forget_password.html", {'error_message':error_message})    

def forget_password_otp(request):
    if request.method == "GET":
        return HttpResponseRedirect('/forget_password/')
    
    # RETRIVE FORM DATA
    email = request.POST["email"]
    otp = request.POST["otp"]
    new_password = request.POST["new_password"]
    confirm_password = request.POST["confirm_password"]
    
    if int(otp) == 0:
        error_message = "Incorrect OTP."
        return render(request, "user/forget_password_otp.html", {'error_message' : error_message, "email" : email})

    if new_password != confirm_password:
        error_message = "Password don't match."
        return render(request, "user/forget_password_otp.html", {'error_message' : error_message, "email" : email})

    # ACCESS USER FROM DATABASE
    user = User.objects.filter(email = email)
    if user:
        if user[0].otp == int(otp):
            user[0].password = new_password
            user[0].otp = None
            user[0].save()
            success_message = "Password has been changed successfully."         
            return render(request, "user/login.html", {'success_message' : success_message})
            
    error_message = "Incorrect OTP."
    return render(request, "user/forget_password_otp.html", {'error_message' : error_message, "email" : email})

def resend_otp(request):
    if request.method =="GET":
        return HttpResponseRedirect('/forget_password/')
    
    try:
        # RETRIVE FORM DATA
        email = request.POST["email"]

        # ACCESS USER FROM THE DATABASE
        user = User.objects.get(email = email)
                    
        # SEND NEW OTP TO EMAIL
        otp = random.randint(1000,9999)
        user.otp = otp
        user.save()
        mail_subject = "OTP"
        mail_message = str(otp) + " is your OTP to change you password in your FoodBlog."
        send_otp_mail(mail_subject, mail_message, user.email)
        success_message = "New OTP has been sent to this email address."
        return render( request, "user/forget_password_otp.html", {'success_message' : success_message, "email" : user.email})
    
    except:
        error_message = "Email does not exist."
        return render(request, "user/forget_password.html", {'error_message':error_message})    

def profile (request):
    # CHECK IF SESSION IS AVAILABLE
    if "email" in request.session:
        user = User.objects.get(email = request.session["email"])
        return render(request, "user/profile.html", {"user" : user})
    
    # CHECK IF COOKIES ARE AVAILABLE
    elif request.COOKIES.get('email'):
        cookie_data = {
            'email': request.COOKIES.get('email'),
            'password': request.COOKIES.get('password'),
        }
        return render(request, "user/login.html", {"cookie_data": cookie_data})
    
    else:
        return HttpResponseRedirect('/login/')

def change_password(request):
    # CHECK IF SESSION IS AVAILABLE
    if "email" in request.session:
        return render(request, "user/change_password.html")
    return HttpResponseRedirect('/login/')

def update_profile_user(request):
    if request.method == "GET":
        if "email" in request.session:
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/login/')
    else:
        # RETRIVE FORM DATA
        username = request.POST["username"]
        user = User.objects.get(email = request.session["email"])

        # UPDATE PROFILE
        user.username = username
        user.save()
        request.session["username"] = username
        return HttpResponseRedirect('/')    

def change_password_user(request):
    if request.method == "GET":
        if "email" in request.session:
            return HttpResponseRedirect('/change_password/')
        return HttpResponseRedirect('/login/')
    
    else:
        # RETRIVE FORM DATA
        current_password = request.POST["current_password"]
        new_password = request.POST["new_password"]
        retype_new_password = request.POST["retype_new_password"]
        
        if new_password != retype_new_password:
            error_message = "Password don't match."
            return render(
                request, 
                "user/change_password.html", 
                {'error_message' : error_message}
            )
        
        else:
            user = User.objects.get(email = request.session["email"])
            if user.password != current_password:
                error_message = "Incorrect Password."
                return render(
                    request, 
                    "user/change_password.html", 
                    {'error_message' : error_message}
                )
            else:
                user.password = new_password
                user.save()
                success_message = "Password has been changed successfully."         
                return render(
                    request, 
                    "user/profile.html", 
                    {'success_message' : success_message, "user" : user}
                )

def logout(request):
    # CHECK IF SESSION IS AVAILABLE
    if "email" in request.session:
        # CLEAR SESSION
        request.session.flush()
    return HttpResponseRedirect('/')



def addProductToCart(customer_id, product_id, size, color, quantity):
    try:
        customer = Customer.objects.get(id = customer_id)
        product = Product.objects.get(id = product_id)
        color = ColorVariation.objects.get(name = color)
        size = SizeVariation.objects.get(name = size)
        if quantity == 0: quantity = 1

        # CHECK IF SAME PRODUCT FOR SAME CUSTOMER WITH EXACT SIZE AND COLOR EXIST IN CART
        if len(CartData.objects.filter(customer = customer, product = product, color = color, size = size)) == 0:
            CartData.objects.create(customer = customer, product = product, color = color, size = size, quantity = quantity)

    except:
        pass

def addToCart(request):
    try:
        # RETRIVE FORM DATA
        customer_id = request.session["customer_id"]
        product_id = request.POST["product_id"]
        size = request.POST["size"]
        color = request.POST["color"]
        quantity = request.POST["quantity"]
        
        addProductToCart(customer_id, product_id, size, color, quantity)
        return HttpResponseRedirect('/cart/')

    except:
        return HttpResponseRedirect('/cart/')

def addToWishlist(request, product_id):
    try:
        customer_id = request.session["customer_id"]
    
        # CHECK IF SAME PRODUCT FOR SAME CUSTOMER EXIST IN WISHLIST
        if len(WishlistData.objects.filter(customer_id = customer_id, product_id = product_id)) == 0:
            WishlistData.objects.create(customer_id = customer_id, product_id = product_id)
        return HttpResponseRedirect('/wishlist/')

    except:
        return HttpResponseRedirect('/wishlist/')

def wishlistToCart(request):
    try:
        # RETRIVE FORM DATA
        customer_id = request.session["customer_id"]
        wishlist_id = request.POST["wishlist_id"]
        product_id = request.POST["product_id"]
        size = request.POST["size"]
        color = request.POST["color"]
        quantity = request.POST["quantity"]
        
        addProductToCart(customer_id, product_id, size, color, quantity)
        return removeFromWishlist(request, wishlist_id)
    
    except:
        return HttpResponseRedirect('/wishlist/')

def removeFromCart(request,cart_id):
    try:
        cart = CartData.objects.get(id=cart_id)
        cart.delete()
        return HttpResponseRedirect('/cart/')
    except:
        return HttpResponseRedirect('/cart/')

def removeFromWishlist(request,wishlist_id):
    try:
        wishlist = WishlistData.objects.get(id=wishlist_id)
        wishlist.delete()
        return HttpResponseRedirect('/wishlist/')
    except:
        return HttpResponseRedirect('/wishlist/')

def cartQuantityIncrement(request, cart_id):
    try:
        cart = CartData.objects.get(id=cart_id)
        cart.quantity = cart.quantity + 1
        cart.save()
        return HttpResponseRedirect('/cart/')
    except:
        return HttpResponseRedirect('/cart/')

def cartQuantityDecrement(request, cart_id):
    try :
        cart = CartData.objects.get(id=cart_id)
        cart.quantity = cart.quantity - 1
        if cart.quantity == 0:  return removeFromCart(request, cart_id)
        cart.save()
        return HttpResponseRedirect('/cart/')
    except:
        return HttpResponseRedirect('/cart/')



def placeOrder(request):
    if request.method == "GET":
        return HttpResponseRedirect('/cart/')

    # RETRIVE CART ITEMS
    cartData = CartData.objects.filter(customer_id = request.session["customer_id"])

    # CHECK IF QUANTITY IS OUT OF STOCK
    for cartItem in cartData:
        if cartItem.quantity > cartItem.product.stock:
            return HttpResponseRedirect('/cart/')

    # RETRIVE FORM DATA
    customer_id = request.session["customer_id"]
    country = request.POST["country"]
    name = request.POST["first_name"] + " " + request.POST["last_name"]
    address_line_1 = request.POST["address_line_1"]
    address_line_2 = request.POST["address_line_2"]
    city = request.POST["city"]
    state = request.POST["state"]
    zip_code = request.POST["zip_code"]
    number = request.POST["number"]
    amount_in_inr_paisa = int(request.POST["grand_total"]) * 100
    
    # USE STRIPE API TO CREATE A CUSTOMER
    customerDetails = stripe.Customer.create(
        email = request.session["email"],
        name = name,
        source = request.POST["stripeToken"],
        address={
            'line1': address_line_1,
            'line2': address_line_2,
            'postal_code': zip_code,
            'city': city,
            'state': state,
            'country': country,
        }
    )
    
    # USE STRIPE API TO MAKE PAYMENT
    charge = stripe.Charge.create(
        customer = customerDetails,
        amount = amount_in_inr_paisa,
        currency = 'inr',
        description = 'rab_fashion_order'
    )
    
    # STORE THE BILLING ADDRESS INTO THE DATABASE
    address = Address.objects.create(customer_id=customer_id, name=name, address_line_1=address_line_1, address_line_2=address_line_2, city=city, state=state, country=country, zip_code=zip_code, contact_no=number)

    # SAVE PAYMENT DETAILS
    payment = Payment.objects.create(amount=(amount_in_inr_paisa/100), payment_method="Card", successfull=True)

    # CREATE A NEW ORDER FOR THE CUSTOMER
    order = Order.objects.create(customer_id=customer_id, status="Ordered", address=address, payment=payment)
    
    # STORE THE CART ITEMS IN ORDERED ITEMS AND DECREASE THE STOCK OF THE PRODUCTS
    for cartItem in cartData:
        # ADD TO ORDERED ITEMS
        OrderItem.objects.create(order=order, product=cartItem.product, color=cartItem.color, size=cartItem.size, quantity=cartItem.quantity, price=cartItem.product.price)
        
        # DECREASE STOCK
        product = Product.objects.get(id=cartItem.product_id)
        product.stock = product.stock - cartItem.quantity
        if product.stock <= 0:
            product.active = False
        product.save()

    # CLEAR THE CART
    cartData.delete()
    request.session["cart_length"] = 0
    
    return HttpResponseRedirect('/order_complete/')

def orders(request):
    if "email" not in request.session:
        return HttpResponseRedirect("/login/")
    
    orders = Order.objects.filter(customer_id=request.session["customer_id"])

    orders_length = len(orders)
    
    return render(request, "user/orders.html",{"orders": orders})

def orderSingle(request):
    if request.method == "GET":
        return HttpResponseRedirect("/login/")
    
    order_items = OrderItem.objects.filter(order_id = request.POST["order_id"])
    return render(request, "user/order_single.html",{"order_items": order_items})
