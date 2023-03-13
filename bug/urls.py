from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/bugs', views.bugs, name='bugs-data'),
]