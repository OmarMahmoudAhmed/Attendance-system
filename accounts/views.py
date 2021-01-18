from django.contrib.auth.forms import AuthenticationForm
from accounts.models import UserRegister
from django.shortcuts import render
from .form import UserRegisterForm
from .models import UserRegister
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save()
            '''
            username = form.changed_data['username']
            password = form.changed_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            '''
            #return redirect('')
    else:
        form = UserRegisterForm
    
    return render(request, 'registration/SignUpForm.html', {'form' : form })
    
