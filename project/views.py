from django.shortcuts import render, redirect
from .forms import addProjectForm

# Create your views here.

def add_project(request):
    form=addProjectForm()

    if request.method=="POST":
        form =addProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form=addProjectForm()

    return render(request, 'project/add-project.html',{'form':form})


def projects(request):
    return render(request,'project/projects.html')

