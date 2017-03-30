from django.shortcuts import render, HttpResponse


# Create your views here.
def index (request):
    return render(request, 'turtles/index.html')


def turtlecolor(request, color):

    src = ""
    if color == "red":
        color = "RED"
    elif color == "blue":
        color = "BLUE"
    elif color == "orange":
        color = "ORANGE"
    elif color == "purple":
        color = "PURPLE"
    else:
        color = "NOTAPRIL"

    context = {
    "color" :color

    }


    return render(request, 'turtles/turtlecolor.html', context)
