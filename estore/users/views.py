from django.shortcuts import render

# Create your views here.

def welcome_page(request):
    return render(request,"users/startpage.html")


def homepage(request):
    return render(request,"users/homepage.html")


def books_page(request):
    return render(request,"users/bookpage.html"),