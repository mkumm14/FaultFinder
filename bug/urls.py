from django.urls import path
from . import views
urlpatterns = [
    path('projects/<int:pk>/bugs', views.bugs, name='project-bugs'),
]