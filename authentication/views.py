from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm, editUserForm, editUsernameForm
from django.contrib import messages
from django.urls import reverse
from django.template.context_processors import csrf
from django.http import JsonResponse
from crispy_forms.utils import render_crispy_form
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView


# Create your views here.


class CustomLoginView(LoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authentication'] = True
        return context


def username(request):
    return render(request, 'user/partials/username.html')

def username_partial(request,pk):
    user=User.objects.get(id=pk)
    return render(request,'user/partials/username_partial.html',{'user':user})


def edit_username(request, pk):
    user=User.objects.get(id=pk)
    if request.method=="POST":
        form=editUsernameForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # return redirect( reverse('username-partial', kwargs={'pk': user.id}))
            response=render(request, 'user/partials/username_partial.html',{'user':user})
            response['Hx-Trigger'] = 'username-changed'
            return response
    else:
        form=editUsernameForm(instance=user)
    return render(request,'user/partials/edit-username.html',{'user':user,'form':form})



def user_info(request):
    return render(request, 'user/partials/user-info.html')



def edit_user(request, pk):
    user=User.objects.get(id=pk)
    if request.method=="POST":
        form=editUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-info')
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
    return render(request,'authentication/register.html',{'form':form,"authentication":True})




def logout_view(request):
    logout(request)
    return redirect('index')
