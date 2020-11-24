from django.shortcuts import render

# Create your views here.
app_name='users'
def welcome_page(request):
    return render(request,"users/startpage.html")


def homepage(request):
    return render(request,"users/homepage.html")

def book_page(request):
    return render(request,"users/bookpage.html")

def buy_sell(request):
    return render(request,"users/buy-sell.html")

def get_notes(request):
    return render(request,"users/notes.html")

def get_equip(request):
    return render(request,"users/project-lab-equip.html")

def get_stationery(request):
    return render(request,"users/stationery.html")