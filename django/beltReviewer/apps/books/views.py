from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import Book
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
    return render(request, 'books/welcome.html')

def loginFormAction (request):

    return redirect(reverse('books' ), 'books/library.html', context)

def registerFormAction(request):
    print "________________________"
    firstname = request.POST['registerFirst']
    lastname = request.POST['registerLast']
    email = request.POST['registerEmail']
    password = request.POST['registerPassword']
    password2 = request.POST['registerPasswordConfirm']
    is_true = True
    if len(firstname) < 2:
        is_true = False
    if len(lastname) < 2:
        is_true = False
    if not email_regex.match(email):
        is_true = False
    if not password == password2:
        is_true = False
    if is_true == True:

    return render(request, 'books/library.html')

def addBook(request):
    return render(request, 'books/addbook.html')

def bookPage (request, id):
    newbook = Book.objects.create(title = request.POST['bookTitle'], author = request.POST['bookAuthor'])
    return redirect(reverse('books:bookProfile', kwargs = {'id':newbook.id}))

def bookProfile(request, id):
    context = {
    'book' : Book.objects.filter(id = id),
    }
    return render(request, 'books/bookpage.html', context)


def library(request):
    context = {
    'all_books' : Book.objects.all()
    }
    return render(request, 'books/library.html', context)

def displayUser(request, id):
    return render(request, 'books/showUser.html')
