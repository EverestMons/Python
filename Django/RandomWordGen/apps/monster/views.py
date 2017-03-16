from django.shortcuts import render, HttpResponse, redirect
import random
import string


# Create your views here.
def index(request):

    return render(request,'monster/index.html')
    # {'value' :value + word})

#
# def create(request):
#  if request.method == "POST":
#   print "*"*50
#   print request.POST
#   print request.method
#   print "*"*50
#   return redirect("/")
#  else:
#   return redirect("/")


def create (request):
    request.session['word'] = request.POST['letters']
    request.session['word'] += random.choice(string.ascii_letters)

    print "++++++++++++++++++++++++++++++++++++++++++++++++"
    print request.session['word']
    return redirect('/')
