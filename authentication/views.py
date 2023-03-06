from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib import messages
from django.template.context_processors import csrf
from django.http import JsonResponse
from crispy_forms.utils import render_crispy_form

from django.contrib.auth import login, authenticate, logout

# Create your views here.

def profile_view(request):
    return render(request, 'user/user_profile.html')


def register_view(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=RegisterForm()
    return render(request,'authentication/register.html',{'form':form})




def logout_view(request):
    logout(request)
    return redirect('index')
