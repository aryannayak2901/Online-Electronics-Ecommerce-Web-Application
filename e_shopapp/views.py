from itertools import product
import numbers
from os import remove
from time import sleep
from turtle import update
from unicodedata import category, name
from urllib import response
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from datetime import datetime
from e_shopapp.models import Contact, Product, Orders, OrderUpdate, User_details
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from e_shop import settings
from django.core.mail import send_mail, EmailMessage
import random
import json
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum



from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from .forms import SignupForm







MERCHANT_KEY = 'kbzk105bJiV_03p5'

# Create your views here.


def index(request):
    products = list(Product.objects.all())
    # print(products)
    product_home_page = random.sample(products, 10)
    # print(product_home_page)
    # print(Product.objects.all())
    product_list = 8
    n = random.randint(1, 8)
    param = {
        'product': product_home_page,
        'range': range(product_list),
        'n': str(n)
    }
    # print("The value is "+param['product'])

    context = {
        "variable": "This is sent"
    }
    return render(request, "index.html", param)


def about(request):
    return render(request, "about.html")
    # return HttpResponse('Hi this is the About Page.')


def services(request):
    return render(request, 'services.html')
    # return HttpResponse('Hi this is the Sevices Page.')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        contact = Contact(name=name, email=email,
                          message=message, phone=phone, date=datetime.today())
        contact.save()
        messages.success(request, 'You have successfully sent a message.!')

    return render(request, 'contact.html')
    # return HttpResponse('Hi this is the Contact Page.')


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # messages.success(request, 'You have successfully signed in.!')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully signed in.!')
            global user_name_for_user_profile
            user_name_for_user_profile = User.objects.filter(username = username)
            print('following is the user')
            print(user_name_for_user_profile)
            print('above is the user')
            return redirect('/user_profile')
        else:
            messages.error(request, "You have entered wrong Credentials.!")
            return render(request, 'signin.html')
        

    return render(request, 'signin.html')






def signup(request):  
    if request.method == 'POST':  
        to_email = request.POST.get("email")
        print('Hi this is 1st.')
        form = SignupForm(request.POST) 
        print(form)
        # def val():
        #     print('Hi this is 2nd.') 
        #     email = forms.EmailField(max_length=200, help_text='Required')

        #     print('Hi this is 3rd.')
        #     model = User  
        #     fields = ('username', 'email', 'password1', 'password2')
        #     return form.is_valid
        # val()

        # form.is_valid = True 
    
        

        if 0 < 1: 
            print('Hi this is 4th.') 
            # save form in the memory not in database  
            # users = form.save()  
            # users.is_active = False  
            # users.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('acc_active_email.html', {  
                # 'user': users,  
                'domain': current_site.domain,  
                # 'uid':urlsafe_base64_encode(force_bytes(users.pk)),  
                # 'token':account_activation_token.make_token(users),  
            })  
            # to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            print('Hi this is 5th.')
            return redirect('/signin')
        else:
            print('Not Valid')  
    else:  
        form = SignupForm()  
    return render(request, 'signup.html') 

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')











# def signup(request):

#     letters_capital_for_user_id = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
#                                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#     letters_small_for_user_id = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#                                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#     numbers_for_user_id = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#     letters_of_capital_id = ''
#     letters_of_small_id = ''
#     numbers_for_id = ''
#     for l in range(0, 2):
#         user_id_from_capital_letters = random.randint(0, 25)
#         letters_of_capital = letters_capital_for_user_id[user_id_from_capital_letters]
#         letters_of_capital_id = letters_of_capital_id + letters_of_capital

#     for l in range(0, 2):
#         user_id_from_small_letters = random.randint(0, 25)
#         letters_of_small = letters_small_for_user_id[user_id_from_small_letters]
#         letters_of_small_id = letters_of_small_id + letters_of_small

#     for n in range(0, 2):
#         numbers = random.randint(0, 9)
#         numbers_id = numbers_for_user_id[numbers]
#         numbers_for_id = numbers_for_id + numbers_id

#     user_id = letters_of_capital_id + numbers_for_id + letters_of_small_id

#     if request.method == "POST":
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         password = request.POST.get('password')
#         confirmation_password = request.POST.get('confirmation_password')
#         # id = user_id
#         address = request.POST.get('address')
#         address2 = request.POST.get('address2')
#         city = request.POST.get('city')
#         zip = request.POST.get('zip')

#         if User.objects.filter(username=username):
#             messages.error(
#                 request, 'This username is already taken use another username.!')

#             return redirect('/signup')

#         if User.objects.filter(email=email):
#             messages.error(
#                 request, 'This email is already registered use another email.!')

#             return redirect('/signup')

#         if len(username) > 10:
#             messages.error(request, 'Username must be under 10 characters.!')

#         if confirmation_password != password:
#             messages.error(request, "Password dosen't matches.!")
#             return redirect('/signup')

#         if not username.isalnum():
#             messages.error(request, 'Username must be a alphanumeric.!')
#             return redirect('/signup')

#         myuser = User.objects.create_user(username, email, password)
#         myuser.firstname = firstname
#         myuser.lastname = lastname

#         myuser.save()
#         if request.method == "POST":
#             first_name = request.POST.get('firstname')
#             last_name = request.POST.get('lastname')
#             phone_number = request.POST.get('phone_number')
#             address = request.POST.get('address')
#             address2 = request.POST.get('address2')
#             city = request.POST.get('city')
#             zip = request.POST.get('zip')
#             user_image = request.POST.get('image')
            
#             user_details = User_details(first_name = first_name, last_name = last_name, phone_number = phone_number, address = address, address2 = address2, city = city, zip = zip, user_image = user_image)

#             user_details.save()

#         # user_personal_detail = User.objects(address, address2)

#         # user_personal_detail.save()

#         messages.success(request, 'You have successfully signed up.!')

#         # print(settings.EMAIL_HOST_USER, settings.EMAIL_HOST, settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD, settings.EMAIL_PORT)

#         # send_mail(
#         #     'Welcome to e_shop -Login!!',
#         #     'Hello" + myuser.firstname + "!! \n" + "Welcome to e_shop!! \n Thankyou for visiting our website. \n We have also sent you a confirmation email, please confirm your email address in order to activate your account. \n  We have sent you a confirmation email so confirm your email. \n\n Thanking You \n Nayak Aryan and Pandya Aryan',
#         #     'eshopweb2901@gmail.com',
#         #     ['tech2aryan2901@gmail.com'],
#         #     fail_silently=False,
#         # )


#         # email = EmailMessage(
#         #     'Welcome to e_shop -Login!!',
#         #     'Hello" + myuser.firstname + "!! \n" + "Welcome to e_shop!! \n Thankyou for visiting our website. \n We have also sent you a confirmation email, please confirm your email address in order to activate your account. \n  We have sent you a confirmation email so confirm your email. \n\n Thanking You \n Nayak Aryan and Pandya Aryan',
#         #     settings.EMAIL_HOST_USER,
#         #     ['tech2aryan2901@gmail.com'],
#         # )

#         # email.fail_silently = False
#         # email.send()

#         # Welcome Mail
#         # print(settings.EMAIL_HOST_USER)
#         # print(myuser.email)
#         subject = "Welcome to e_shop -Login!!"
#         message = "Hello" + myuser.firstname + "!! \n" + "Welcome to e_shop!! \n Thankyou for visiting our website. \n We have also sent you a confirmation email, please confirm your email address in order to activate your account. \n  We have sent you a confirmation email so confirm your email. \n\n Thanking You \n Nayak Aryan and Pandya Aryan"
#         from_email = settings.EMAIL_HOST_USER
#         to_list = [myuser.email]
#         send_mail(subject, message, from_email, to_list)

#         return redirect('/signin')

#     return render(request, 'signup.html')


def signout(request):
    logout(request)
    messages.success(request, 'You have successfully signed out.!')

    return redirect('/')





# def cart(request):

#     request.session.modified = True
    # for key in list(request.session.keys()):
    #     del request.session[]
    
    # For clear all the user Data from session.
    # request.session.clear()
    
    # For clear all items from cart.
    # request.session.get('cart').clear()
    
    
    # products = list(Product.objects.all())
    # cart_product = request.POST.get('item_of_cart')
    # cart = []
    
    # if cart:
    #     quantity = cart.get(cart_product)
    #     if quantity:
    #         cart[cart_product] = quantity + 1
    #         # if remove:
    #         #     cart[cart_product] = quantity - 1
    #     else:
    #         cart[cart_product] = 1
    # else:
    #     cart = {}
    #     cart[cart_product] = 1

    # ids = list(cart.keys())
    # print(ids)
    # print(ids)
    # print(ids)
    # print(ids)
    # print(ids)
    # print(ids)
    
    # global product_list_for_cart
    # product_list_for_cart = Product.objects.filter(id__in = ids[1:])
    # print(product_list_for_cart)

    

    # products = list(Product.objects.all())
    # print(products)
    # remove = request.POST.get('remove')
    # print()
    # cart_product = request.POST.get('item_of_cart')
    # cart = request.session.get('cart')

    # if cart:
    #     quantity = cart.get(cart_product)
    #     if quantity:
    #         cart[cart_product] = quantity + 1
    #         # if remove:
    #         #     cart[cart_product] = quantity - 1
    #     else:
    #         cart[cart_product] = 1
    # else:
    #     cart = {}
    #     cart[cart_product] = 1
        

    # request.session['cart'] = cart
    # # cart_list = list(cart)
    # print(request.session['cart'])
    # # print(cart_list)

    # ids = list(request.session.get('cart').keys())
    # print("ids" + str(ids[1:]))
    # print(ids)
    
    # global product_list_for_cart
    # product_list_for_cart = Product.objects.filter(id__in = ids[1:])
    # print(product_list_for_cart)

    
    # cart_items_length = len(product_list_for_cart)

    # print(product_list_for_cart)
    # cart_list = Product.get_products_by_id(ids)
    # print(cart_list)
    
    # param_cart = {
    #     'product_list_for_cart': product_list_for_cart,
    #     'cart_items_length': cart_items_length
    # }

    # return product_list_for_cart



    # Product.objects.all()
    # request.session.get('cart_list')
    # cart_list = []
    # item_of_cart = request.POST.get('item_of_cart')
    # # request.session.get('cart')

    # # if cart:
    # #     cart['product'] = 1
    # # else:
    # print(Product.objects.all())
    # print(cart_list)


    # if item_of_cart in cart_list:
    #     item_of_cart = None
    # else:
    #     cart_list.append(item_of_cart)
    # print(item_of_cart)
    
    # param_cart = {
    #     'cart_list': cart_list
    # }
    # product_list = {
    #     "product_id": Product.objects.filter(id = )
    # }
    # return render(request, 'cart.html', param_cart)


def upload_product(request):

    if request.method == "POST":
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        seller_name = request.POST.get('seller_name')
        image = request.FILES['image'];
        
        product = Product(product_name = product_name, category = category, subcategory = subcategory, price = price, desc = desc, seller_name = seller_name, image = image)

        product.save()
    
    
        
    last_added_product = (Product.objects.last()).id

    print('abcdefghi')
    print(last_added_product)
    print('abcdefghi')

    selling_product_list_for_user_profile = request.session.get('selling_product_list_for_user_profile')

    if selling_product_list_for_user_profile:
        selling_product_list_for_user_profile[last_added_product] = 1
    else:
        selling_product_list_for_user_profile = {}
        selling_product_list_for_user_profile[last_added_product] = 1

    request.session['selling_product_list_for_user_profile'] = selling_product_list_for_user_profile
        
    selling_product_list_ids = list(request.session.get('selling_product_list_for_user_profile').keys())

    print('below is the ids')
    print(selling_product_list_ids, 'idsssss')

    def clear_true(y):
        if y == 'True':
            return False
        else:
            return True
    selling_product_list_ids = list(filter(clear_true, selling_product_list_ids))
    print(selling_product_list_ids, 'idsssss')

    def clear_null(y):
        if y == 'null':
            return False
        else:
            return True
        
    selling_product_list_ids = list(filter(clear_null, selling_product_list_ids))
    print(selling_product_list_ids, 'idsssss')
        
    global product_list_for_selling_list_for_user_profile
    product_list_for_selling_list_for_user_profile = Product.objects.filter(id__in = selling_product_list_ids[:])

        # selling_product_ids = list(request.session.get('selling_product_list_for_user_profile').keys())
        # print('below is the selling_product_ids')
        # print(selling_product_ids)
        # print(selling_product_ids)
        # print(selling_product_ids)
        # print(selling_product_ids)
        # print(selling_product_ids)
        # print(selling_product_ids)

        # print("selling product list")
        # print(selling_product_list_for_user_profile)
        # print(selling_product_list_for_user_profile)
        # print(selling_product_list_for_user_profile)
        # print(selling_product_list_for_user_profile)
        # print(selling_product_list_for_user_profile)
        # print(selling_product_list_for_user_profile)
        # print("selling_product_list")

        # print("selling product list")
        # print(last_added_product)
        # print(last_added_product)
        # print(last_added_product)
        # print(last_added_product)
        # print(last_added_product)
        # print(last_added_product)
        # print("selling_product_list")    

    print(request.FILES)
    print(request.FILES)
    print(request.FILES)
    print(request.FILES)

    return render(request, 'upload_product.html')


def product_view(request, product_view_page_product_id):
    product_view = Product.objects.filter(id = product_view_page_product_id)
    print(product_view)
    return render(request, 'product_view.html', {'product_view': product_view[0]})


def cart_list(request):

    # for empty cart list
    # del request.session['cart']

    # request.session.modified = True    
    
    # products = list(Product.objects.all())
    

    def checkout_item_list():
        # del request.session['checkout_list']
        checkout_list = request.session.get('checkout_list')
        item_of_checkout = request.POST.get('item_of_checkout')
        add_to_checkout = request.POST.get('add_to_checkout')
        

        if request.method == "POST":
            delete_button_for_checkout = request.POST.get('delete_button_for_checkout')
            if delete_button_for_checkout:
                checkout_list.pop(delete_button_for_checkout)
                messages.success(request, 'Product has been removed.!')
                # return HttpResponseRedirect('/checkout')


        
        
        global item_price_for_checkout
        item_price_for_checkout = add_to_checkout

        print(add_to_checkout, 'checkouttttttttttttttttttttttttttttttttttt')
        print(add_to_checkout)
        print(add_to_checkout)

        print(item_of_checkout)
        print(item_of_checkout)
        print(item_of_checkout)

        print()

        if checkout_list:
            quantity = checkout_list.get(item_of_checkout)
            if quantity:
                checkout_list[item_of_checkout] = quantity + 1
            else:
                checkout_list[item_of_checkout] = 1
        else:
            checkout_list = {}
            checkout_list[item_of_checkout] = 1

        request.session['checkout_list'] = checkout_list
        checkout_ids = list(request.session.get('checkout_list').keys())
        print('below is the ids')
        print(checkout_ids, 'idsssss')
        def clear_true(y):
            if y == 'True':
                return False
            else:
                return True
        checkout_ids = list(filter(clear_true, checkout_ids))
        print(checkout_ids)

        def clear_null(y):
            if y == 'null':
                return False
            else:
                return True
        
        checkout_ids = list(filter(clear_null, checkout_ids))

        print('below is the checkout list items')
        print(checkout_ids)
        print(checkout_ids)
        print(checkout_ids)
        print(checkout_ids)
        print('above is the checkout list items')
        
        
        global product_list_for_checkout
        product_list_for_checkout = Product.objects.filter(id__in = checkout_ids[:])
        print('hi')
        print('hi')
        print('hi')
        print('hi')
        print('hi')
        
        checkout_item_length = len(checkout_ids)

        item_price_list_for_checkout = []
        for j in product_list_for_checkout:
            item_price_list_for_checkout.append(j.price)

        shipping_charge_for_checkout_page = 150

        global item_total_price_for_checkout
        item_total_price_for_checkout = sum(item_price_list_for_checkout) + shipping_charge_for_checkout_page
        print('below is the total price for checkout')
        print(item_total_price_for_checkout)

        return product_list_for_checkout, checkout_item_length, item_total_price_for_checkout

        # print(item_of_checkout)
    
    def cart_item_list():
        # del request.session['cart']
        cart_product = request.POST.get('item_of_cart')
        cart = request.session.get('cart')
        delete_button = request.POST.get('delete_button')

        if delete_button:
            cart.pop(delete_button)        

        print('below is the delete button')
        print(delete_button)
        print(delete_button)
        print(delete_button)
        print(delete_button)
        print(delete_button)
        print('above is the delete button')
        # item_price_for_cart = request.POST.get('item_price_for_cart')
        # item_total_price_for_cart = request.session.get('item_total_price_for_cart')


        # Total price in cart
        # item_total_price_for_cart = {}
        # price_of_item = item_total_price_for_cart.get(item_price_for_cart)
        # item_total_price_for_cart[item_price_for_cart] = price_of_item
        # request.session['item_total_price_for_cart'] = item_total_price_for_cart
        # print('Total price is below.')
        # print(request.session['item_total_price_for_cart'])
        # print(item_total_price_for_cart)
        # print(item_total_price_for_cart)
        # print(item_total_price_for_cart)
        # print(item_total_price_for_cart)
        # print(item_total_price_for_cart)

        # print('below is the cart items.')
        # print(item_price_for_cart)
        # print(item_price_for_cart)
        # print(item_price_for_cart)
        # print(item_price_for_cart)
        # print('above is the cart item')
        
        if cart:
            quantity = cart.get(cart_product)
            if quantity:
                cart[cart_product] = quantity + 1
                # if remove:
                #     cart[cart_product] = quantity - 1
            else:
                cart[cart_product] = 1
        else:
            cart = {}
            cart[cart_product] = 1

        request.session['cart'] = cart
        # # cart_list = list(cart)
        # print("hi")
        # print(request.session['cart'])
        # # print(cart_list)

        ids = list(request.session.get('cart').keys())
        # print("hi")
        # print("ids" + str(ids[1:len(ids) - 1]))

        # To delete the null value from ids.
        def clear_null(x):
            if x == 'null':
                return False
            else:
                return True
        
        ids = list(filter(clear_null, ids))

        print('below is the ids')
        print(ids)
        print(ids)
        print(ids)
        print(ids)
        print(ids)
        print('above is the ids')
        
        # for i in ids:
        #     ids.pop(int(i))


        # print('hi ids')
        # print(ids)
        
        global product_list_for_cart
        product_list_for_cart = Product.objects.filter(id__in = ids[:])
        
        item_price_list_for_cart = []
        for i in product_list_for_cart:
            item_price_list_for_cart.append(i.price)
        # print('below is the price list.')
        # print(item_price_list_for_cart)
        # print(sum(item_price_list_for_cart))
        # print('above is the price_list.')
        global item_total_price_for_cart
        item_total_price_for_cart = sum(item_price_list_for_cart)
        print(item_total_price_for_cart)
        
            

        # print('hi')
        # print(product_list_for_cart)
        global cart_items_length
        cart_items_length = len(ids)-1
        print('below is the cart_items_length')
        print(cart_item_list)

        return product_list_for_cart, cart_items_length, item_total_price_for_cart

    final_checkout_list =  checkout_item_list()
    final_cart_list = cart_item_list()
    
    shipping_charge = 150

    total_charge = item_total_price_for_cart + shipping_charge

    print('hi')
    print(final_checkout_list)
    print("hi")
    print(final_cart_list)
    print(item_total_price_for_cart)
    print(item_total_price_for_cart)
    print(item_total_price_for_cart)
    print(item_total_price_for_cart)
    print(item_total_price_for_cart)

    param_cart = {
        'product_list_for_cart': product_list_for_cart,
        'item_total_price_for_cart': item_total_price_for_cart,
        'shipping_charge': shipping_charge,
        'total_charge': total_charge,
        'cart_items_length': cart_items_length
    }

    # products = list(Product.objects.all())
    # cart_product = request.POST.get('item_of_cart')
    # cart = []
    
    # if cart:
    #     quantity = cart.get(cart_product)
    #     if quantity:
    #         cart[cart_product] = quantity + 1
    #         # if remove:
    #         #     cart[cart_product] = quantity - 1
    #     else:
    #         cart[cart_product] = 1
    # else:
    #     cart = {}
    #     cart[cart_product] = 1

    # if cart_product in cart:
    #     pass
    # else:
    #     cart += cart_product

    # ids = cart
    # cart_items_length = len(ids)
    
    # print(ids)

    # global product_list_for_cart
    # product_list_for_cart = Product.objects.filter(id__in = ids)
    # print('hi')
    # print(product_list_for_cart)

    return render(request, 'cart.html', param_cart)


def checkout(request):
    cart_list(request)
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip = request.POST.get('zip')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        total_price = request.POST.get('total_price')
        
        
        submit_checkout_list = request.POST.get('submit_checkout_list')

        if submit_checkout_list:

            print(submit_checkout_list)
            print(submit_checkout_list)
            print(submit_checkout_list)
            print(submit_checkout_list)
            print(submit_checkout_list)
            
            
            
            if submit_checkout_list == 'True':
                global tracker_list
                tracker_list = []
                tracker_list = list(product_list_for_checkout)
            # print(tracker_list)
            # print(tracker_list)
            # print(tracker_list)
            # print(tracker_list)
            
            orders = Orders(product_list_for_checkout = list(product_list_for_checkout), email = email, name = name, address = address, city = city, zip = zip, phone_number = phone_number, total_price = total_price)

            orders.save()

            # global product_list_for_user_profile
            # product_list_for_user_profile = checkout_list
        

            # orders.save()
            id = Orders.objects.all().last()
            print('order id is below.')
            print(id, 'idddddddddddddddddddddddddddd')

            update = OrderUpdate(order_id = orders.order_id, update_desc = "The order has been placed.")
            update.save()

            # request paytm to transfer the amount to your account after payment by user

            param_dict = {

                'MID': 'WorldP64425807474247',
                'ORDER_ID': str(orders.order_id),
                'TXN_AMOUNT': str(total_price),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)

            return render(request, 'paytm.html', {'param_dict': param_dict})

            messages.success(request, 'You have successfully Order a Product. Use it to track your order using our order tracker👍. Your Order id is 👉👉👉👉 ' + str(id) + ' 👈👈👈👈,for track your Order. Thanks you to visit this platform💖!')
            

            return redirect('/tracker')

            # thank = True
            # messages.success(request, 'You have successfully Order a Product.!')

        # else:
        #     product_list_for_user_profile = ['empty']
    # print(product_list_for_cart)
    checkout_list = product_list_for_checkout

    global product_list_for_user_profile
    product_list_for_user_profile = checkout_list

    global product_cart_list_for_user_profile
    product_cart_list_for_user_profile = product_list_for_cart
    param_checkout_list = {
        'checkout_list': checkout_list,
        'item_total_price_for_checkout': item_total_price_for_checkout
    }
    return render(request, 'checkout.html', param_checkout_list)

@csrf_exempt
def handlerequest(request):
    # paytm will sen you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})

def history(request):
    return render(request, 'history.html')


def tracker(request):

    if request.method == "POST":
        OrderId = request.POST.get('OrderId', '')
        email = request.POST.get('email', '')
        print("hi this is track")
        # return HttpResponse(f'{email} and {OrderId}')
        try:
            order = Orders.objects.filter(order_id = OrderId, email = email)
            
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id = OrderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].product_list_for_checkout], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'tracker.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Product.objects.none()
    else:
        allPostsTitle= Product.objects.filter(product_name__icontains=query)
        allPostsCategory= Product.objects.filter(category__icontains=query)
        allPostsSubcategory= Product.objects.filter(subcategory__icontains=query)
        allPostsContent = Product.objects.filter(desc__icontains=query)
        allPostsPrice = Product.objects.filter(price__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent).union(allPostsCategory).union(allPostsPrice).union(allPostsSubcategory)
        
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'search.html', params)

def user_profile(request):
    upload_product(request)

    if request.method == "POST":
        delete_button_for_selling_product_list = request.POST.get('delete_button_for_selling_product_list')
        
        if delete_button_for_selling_product_list:
            selling_product_list_for_user_profile.pop(delete_button_for_selling_product_list)
            messages.success(request, 'Product has been removed.!')

    # if request.method == "POST":
    #     product_name = request.POST.get('product_name')
    #     category = request.POST.get('category')
    #     subcategory = request.POST.get('subcategory')
        

    
    product_list = request.POST.get('checkout_item_list_for_user_profile')
    checkout(request)
    print('below is the item list👇')
    print(product_list_for_user_profile)
    print(product_list_for_cart)
    print('above is the item list👆')

    selling_product_list_for_user_profile = product_list_for_selling_list_for_user_profile
    
    param_user_profile = {
        'product_list_for_user_profile': product_list_for_user_profile,
        'product_cart_list_for_user_profile': product_list_for_cart,
        'selling_product_list_for_user_profile': selling_product_list_for_user_profile
    }
    
    # print('follow is the user')
    # signin(request)
    # print(user_name_for_user_profile)
    # print('above is the user')
    
    # user_profile_details = User.objects.filter(username = user_name_for_user_profile).first()
    # print('user profile details is below or following.')
    # print(str(user_profile_details))
    # print(User.objects.all())
    return render(request, 'user_profile.html', param_user_profile)

