from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm, editUserForm
from django.contrib import messages
from django.template.context_processors import csrf
from django.http import JsonResponse
from crispy_forms.utils import render_crispy_form
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def edit_user(request, pk):
    user=User.objects.get(id=pk)
    if request.method=="POST":
        form=editUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'user/partials/user-info.html')
    else:
        form=editUserForm(instance=user)
    return render(request, 'user/partials/edit-user.html', {'form':form,'user':user})



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
