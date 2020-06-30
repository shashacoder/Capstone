#from django.shortcuts import render
import json
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def splash(request):
    return render(request, 'splash.html')

def login(request):
    if request.method=="POST":
  #  return render(request, 'login.html');
        ta=request.POST["tab"]
        if ta=="Sign In":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('topic')
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('login')

        else:
              username = request.POST['username1']
              password1 = request.POST['password1']
              password2 = request.POST['password2']
              email = request.POST['email']

              if password1 == password2:
                  if User.objects.filter(username=username).exists():
                      messages.info(request, 'Username Taken')
                      return redirect('login')
                  elif User.objects.filter(email=email).exists():
                      messages.info(request, 'Email Taken')
                      return redirect('login')
                  else:
                      user = User.objects.create_user(username=username, password=password1, email=email)
                      user.save()
                      print('User created')
                      return redirect('login')
              else:
                  messages.info(request, 'Password not matching')
                  return redirect('login')

    else:
        return render(request, 'login.html')


def forgot(request):
 

    return render(request, 'forgot.html')

def question(request):
   
    return render(request, 'question.html')

def topic(request):
    return render(request, 'topic.html')

def end(request):
    return render(request, 'end.html')