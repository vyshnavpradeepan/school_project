# from django.contrib import auth, messages
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
#
#
# def index(request):
#     return render(request, 'index.html')
#
#
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             #return redirect('/')
#             return render(request, 'form.html')
#         else:
#             messages.info(request, 'invalid credentials')
#             #return redirect('login')
#             return render(request, 'login.html')
#     return render(request, "login.html")
#
#
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         # first_name = request.POST['first_name']
#         full_name = request.POST['fullname']
#         # last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         cpassword = request.POST['password1']
#         if password == cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username Already Exist')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Already Exist')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#             user.save();
#             print("user created")
#             return redirect('login')
#         else:
#             messages.info(request, "password not match")
#             return redirect('register')
#         return redirect('/')
#
#     return render(request, "register.html")
#
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
#
#
# def form(request):
#     re = login(request)
#     #return render(request, 'form.html')
#     return re
#
#
# def submit(request):
#     return render(request, 'submit.html')


from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            #return redirect('/')
            return render(request, 'form.html')
        else:
            messages.info(request, 'invalid credentials')
            #return redirect('login')
            return render(request, 'login.html')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        # first_name = request.POST['first_name']
        full_name = request.POST['fullname']
        # last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
            user.save();
            print("user created")
            return redirect('login')
        else:
            messages.info(request, "password not match")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def form_page(request):
    re = login(request)
    #return render(request, 'form.html')
    return re


def submit_form(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials = request.POST.getlist('materials')
        return render(request, 'success.html')

    return render(request, 'form.html')


def submit_form(request):
    if request.method == 'POST':
        message = "Order Confirmed"
        return render(request, 'submit.html', {'message': message})

    return HttpResponse("Invalid request method. Use POST.")
