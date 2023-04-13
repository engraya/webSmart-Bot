# here we are import path from in-built django-urls
from django.urls import path
# here we are importing all the Views from the views.py file
from . import views


# a list of all the urls
urlpatterns = [
    path('', views.home, name='home'),
    path('error/', views.error, name='error'),
    path('errorPage/', views.errorPage, name='errorPage'),
    path('homePage/', views.homePage, name='homePage'),
    path('botPage/', views.botPage, name='botPage'),
]