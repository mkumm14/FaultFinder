from django.shortcuts import render
from project.models import Project
# Create your views here.

def bugs(request, pk):
    project=Project.objects.get(id=pk)
    return render(request, 'bugs/partials/project-bugs.html',{'project':project,"project_view":True})
