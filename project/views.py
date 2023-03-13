from django.shortcuts import render, redirect
from .forms import addProjectForm
from .models import Project
# Create your views here.


def dashboard(request,pk):
    project= Project.objects.get(id=pk)
    return render(request, 'project/dashboard.html',{'project': project})

def add_project(request):
    form=addProjectForm()

    if request.method=="POST":
        form =addProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form=addProjectForm()

    return render(request, 'project/add-project.html',{'form':form})


def projects(request):
    projects=Project.objects.filter(users=request.user)
    return render(request,'project/projects.html',{'projects':projects})

