from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1> Hello World! </h1>")


def my_view(request):
    title = "My Page"
    heading = "Welcome to My Page"
    items = ["Item 1", "Item 2", "Item 3"]
    user = request.user  # Assuming you have authentication set up

    context = {
        'title': title,
        'heading': heading,
        'items': items,
        'user': user,
    }

    return render(request, 'base.html', context)

def my_view2(request):
    title = "My Page"
    heading = "Welcome to My Page"
    items = ["Item 1", "Item 2", "Item 3"]
    user = request.user  # Assuming you have authentication set up

    context = {
        'title': title,
        'heading': heading,
        'items': items,
        'user': user,
    }

    return render(request, 'index.html', context)
