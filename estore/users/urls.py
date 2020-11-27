from django.conf.urls import url
from . import views as user_view


urlpatterns=[
    url('welcome/',user_view.welcome_page),
    url('home/',user_view.homepage,name='homepage'),
    url('books/',user_view.book_page,name='bookpage'),
    url('buy-sell/',user_view.buy_sell,name='buy_sell'),
    url('get-notes/',user_view.get_notes,name='get_notes'),
    url('get-equip/',user_view.get_equip,name='get_equip'),
    url('get_stationery/',user_view.get_stationery,name='get_stationery'),
    url('login_page/',user_view.login_page,name='login_page'),
    url("register/", user_view.register, name="register"),
]