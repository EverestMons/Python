from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from .models import User, UserManager
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your views here.
def index(request):
    return render(request, 'log/index.html')


    # if not last_name.isalpha():
    #     is_true = False
    #     messages.add_message(request, messages.ERROR, 'Name can only be letters')



def registerAction(request):
    success = User.objects.registername(request.POST['index_registration_first'])
    victory = request.POST['index_registration_last']
    # if False:
    #     messages.add_message(request, messages.ERROR, 'Name fields can only be letters')
    email = request.POST['index_registration_email']
    # if False:
    #     messages.add_message(request, messages.ERROR, 'Email must be valid')
    password = request.POST['index_registration_password']
    # request.POST['index_registration_password_confirm'])
    # if False:
    #     messages.add_message(request, message.ERROR, 'Password must be at least 8 characters')
    # if False:
    #     messages.add_message(request, message.ERROR, 'Password must match')
    # return firstname, lastname, email, password
    return redirect('/success')

def hash_password (request):
    password = password.encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed

def enterUser(request):
    User.objects.create(first = firstname, last = lastname, email = email, password = hashed)
    return redirect('/success')

def loginuser(request):
    success = User.objects.login(request.POST['login_email'], request.POST['login_p_word'])
    if success:
        return render(request, 'log/success.html')
    else:
        messages.add_message(request, messages.ERROR, 'No such login')
        return redirect('/')

def success(request):
    context = {
    name: request.session['fname'],
    }
    return HttpResponse ("Hello")
