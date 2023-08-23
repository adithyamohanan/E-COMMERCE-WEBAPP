from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.shortcuts import get_object_or_404
from .forms import ShippingAddressForm
from datetime import datetime




def index(request):
    return render(request, 'index.html')

def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product.html', context)

def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid login")
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            return redirect("register")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.info(request, "Successfully Registered")
            login(request, user)
            return redirect('/')
            return redirect('register')
    else:
        return render(request, 'contact.html')

def logout_view(request):
    logout(request)
    return redirect('/')


def add_Order(request,product):
    if request.user.is_authenticated:
        
        instance = get_object_or_404(Product, id=product)
        orderdetails = order.objects.filter(user=request.user)
        print(orderdetails)
        productname =" "
        for i in orderdetails:
            productname = i.product
        if productname == instance:
            for i in orderdetails:
                i.quantity +=1
                i.save()
        else :
            add = order.objects.create(user=request.user,product=instance,quantity=1)
        previous_page = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(previous_page)
        
        
    else:
        return redirect('login')
    
    return render(request, 'login.html')


def cart_page(request):
    if request.user.is_authenticated:
        
        all_order = order.objects.filter(user=request.user)
        total_no_of_item = order.objects.filter(user=request.user).count()
        total_price = sum(item.product.price * item.quantity for item in all_order)
        print(total_price)
    else:
        all_order = []
        total_no_of_item = 0
        total_price = 0
    context = {
        'all_order':all_order,
        'total_price':total_price,
        'total_no_of_item':total_no_of_item
    } 
    return render(request,'cart.html',context)


def remove_from_cart(request, order_id):
    if request.user.is_authenticated:
        order_item = get_object_or_404(order, id=order_id, user=request.user)
        order_item.delete()
    return redirect('cart_page')


def shipping_address(request):
    form = ShippingAddressForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        address = form.save(commit=False)
        address.user = request.user
        address.save()
        return redirect('cart_page')
    
    
    context = {'form': form}
    return render(request, 'checkout.html', context)


def checkout(request):
    if request.user.is_authenticated:
            
        shipping_form = ShippingAddressForm(request.POST or None)

        if request.method == 'POST':
            if shipping_form.is_valid():
                address = shipping_form.save(commit=False)
                address.user = request.user
                address.save()
    
        all_order = order.objects.filter(user=request.user)
        total_no_of_item = order.objects.filter(user=request.user).count()
        total_price = sum(item.product.price * item.quantity for item in all_order)

        context = {
            'all_order': all_order,
            'total_price': total_price,
            'total_no_of_item': total_no_of_item,
            'shipping_form': shipping_form,
        }

        return render(request, 'checkout.html', context)
    else:
        return redirect('login')
    return render(request, 'login.html')

def update_order_status(request):
    if request.method == 'POST':
        payment_option = request.POST.get('payment_option')
        order_items = order.objects.filter(user=request.user)
        
        for order_item in order_items:
            if payment_option == 'cod':
                order_item.status = 'Confirmed'
            else:
                order_item.status = 'Pending'
                
            order_item.payment_method = payment_option
            order_item.save()
            
            Order_Successful.objects.create(
                user=order_item.user,
                product=order_item.product,
                quantity=order_item.quantity,
                status=order_item.status,
                payment_method=order_item.payment_method,
            )
        order_items.delete()
            
            
        
       
        checkout_redirect = request.POST.get('checkout_redirect')
        return redirect(checkout_redirect)


def track_order(request):
    
    orders = Order_Successful.objects.filter(user=request.user)

    for order_item in orders:
        
        order_item.grand_total = order_item.product.price * order_item.quantity

    context = {'orders': orders}
    return render(request, 'track_order.html', context)

    
    
def reviews(request):
    return render(request, 'testimonial.html')