from django.urls import path
from . import views

app_name = 'StudentRegisteration'

urlpatterns = [
    path('', views.add_student, name='StudentRegisteration'),
]