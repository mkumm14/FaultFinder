from django.shortcuts import render, redirect
from .forms import addProjectForm
from .models import Project
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

# Create your views here.



def dashboard_data(request, pk):
    project=Project.objects.get(id=pk)
    return render(request, 'project/partials/dashboard_data.html', {'project':project})

def dashboard(request,pk):
    project= Project.objects.get(id=pk)
    return render(request, 'project/project-view.html',{'project': project})

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
    
    default_page = 1
    page = request.GET.get('page', default_page)

    projects=Project.objects.filter(users=request.user).order_by('-created_date')
    projects_per_page = 10
    paginator = Paginator(projects, projects_per_page)

    try:
        projects_page = paginator.page(page)
    except PageNotAnInteger:
        projects_page = paginator.page(default_page)
    except EmptyPage:
        projects_page = paginator.page(paginator.num_pages)

    return render(request,'project/projects.html',{'projects':projects_page})

