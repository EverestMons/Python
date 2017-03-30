from django.shortcuts import render, HttpResponse
import random
# Create your views here.
def index(request):
    if request.session['gold'] not in session:
        request.session['gold'] = 0
    return(render(request,'gold/index.html'))

def process(request):
    if request.POST['farm']:
        context = {
        prize : random.randint(15),
        request.session['gold'] : gold + prize
        }
    return(render(request, 'gold/index.html', context))
