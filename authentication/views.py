from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout

# Create your views here.




def register_view(request):
    return render(request,'authentication/register.html')



def logout_view(request):
    logout(request)
    return redirect('index')
