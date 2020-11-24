from django.conf.urls import url
from . import views as user_view


urlpatterns=[
    url('welcome/',user_view.welcome_page,name='welcome'),
    url('',user_view.homepage,name='homepage'),
    url('books/',user_view.books_page,name='booksearch'),
]