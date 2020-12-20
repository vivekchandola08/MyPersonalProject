from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

from datetime import datetime

from Home.models import Contact

from django.contrib import messages

# superuser username=vivek, password->vivek
# username=vicky, password->Vivek@123

# Create your views here.
import nltk
nltk.download('vader_lexicon') 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
def MyNLP(request):
    sid = SentimentIntensityAnalyzer()
    context = {}
    if request.method=="POST":
        msg= request.POST.get('des')
        output = sid.polarity_scores(msg)
        if output.get('compound')==0:
            level = 'Neutral Comment'
        elif output.get('compound')>0:
	        level = 'Positive Comment'
        else:
	        level = 'negative Comment'
        output = str(output)
        context = {
            "output":output,
            "msg":msg,
            "level":level,
        }
    return render(request, 'nlp.html', context)


def contactUser(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')

        print(name, email, phone, desc)

        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    #messages.success(request, 'You Logged In Successfully!')
    return render(request, 'index.html')


def signupUser(request):
    form = RegisterForm()
    if request.method=="POST":
        form = RegisterForm(request.POST)
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/signup')
            else:
                if form.is_valid():
                    print("form is valid")
                    form.save()
                    return redirect('/login')
                else:
                    print("form is not valid")
                    form = RegisterForm()
                    return redirect('/signup')
        else:
            messages.info(request, 'Password not matching...')
            return redirect('/signup')
        
    return render(request, 'signup.html', {'form':form})

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password= password)
        # print(user)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request, 'You Logged In Successfully!')
            return redirect("/")
        else:
            messages.success(request, 'Your Username or password is wrong!')
            # NO backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")



#https://source.unsplash.com/1600x600/?phone
