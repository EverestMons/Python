from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request, 'green/index.html')

def process(request):
    request.session['count'] += 1 
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['location'] = request.POST['location']
    request.session['fav_lang'] = request.POST['fav_lang']
    request.session['comment'] = request.POST['comment']

    return redirect('/success')

def success(request):
    return render(request, 'green/success.html')

def home(request):
    return render(request, 'green/index.html')
