from django.shortcuts import render
from .models import StudentRegisteration
from .form import StudentRegisterationForm
from django.shortcuts import redirect, render
from django.urls import reverse
# Create your views here.


def add_student(request):
    if request.method == 'POST':
        form = StudentRegisterationForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save()
    else:
        form = StudentRegisterationForm
    
    return render(request, 'StudentRegisteration/StudentRegisterationForm.html', {'form' : form })
    



