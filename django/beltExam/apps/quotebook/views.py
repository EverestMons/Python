from django.shortcuts import render, reverse, redirect
from .models import *
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        context = {
        'all_quotes': Quote.objects.all()
        }
        return render(request, 'quotebook/home.html', context)
    return render(request, 'quotebook/login.html')

def addquote(request):
    quote = request.POST['quote']
    author = request.POST['author']
    Quote.objects.create(quote=quote, author=author, users=request.session['user'])
    return redirect('quotebook:home')

def register(request):
    if request.POST['firstname']< 2:
        message.error('Name must be at least 3 characters')
    return render(request, 'quotebook/register.html')
