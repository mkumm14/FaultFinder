from django.urls import path
from . import views
urlpatterns = [
    path('', views.projects, name="projects"),
    path('add-project/',views.add_project, name='add-project'),
    path('<int:pk>/view/',views.project_view,name='project-view')
]
