from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail 
from django.contrib.auth.models import User, auth
from django.conf import settings
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Datos Incorrectos') 
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        message = "Bienvenido a Todo al Paso " + request.POST["username"] + "...Tenemos las mejores ofertas para ti"
        subject = " Supermercado Todo al Paso"
        email_from = settings.EMAIL_HOST_USER

        recipient_list=[email]

        send_mail(subject,message,email_from,recipient_list)



        if password1==password2:
           if User.objects.filter(username=username).exists():
                messages.info(request, 'Usuario ya existe')
                return redirect('register')
           
           else:

               user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
               user.save();
               print('user created')
               return redirect('login')
        else: 
           messages.info(request,'password no son iguales')
           return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

    


def logout(request):
    auth.logout(request)
    return redirect('/')

def cart(request):
    return render(request, 'cart.html')
