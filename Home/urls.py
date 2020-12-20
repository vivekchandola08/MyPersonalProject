#vivek create this file


from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('signup', views.signupUser, name="signup"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('contact', views.contactUser, name="contact"),
    path('about', views.about, name="about"),
    path('nlp', views.MyNLP, name="nlp"),



]


