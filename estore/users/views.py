from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
import json,xmltodict
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

def login_page(request):
    print(request)
    return render(request,"users/login_page.html")#,detail)

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data_dict=dict()
            print("Form Submitted")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            data_dict = xmltodict.parse(form)
            print(json.dumps(data_dict))
            print("------------------------------")
            print(form)
            login(request, user)
            return redirect('users/homepage.html')
    else:
        form = SignUpForm()
    return render(request, 'users/user_reg.html', {'form': form})

