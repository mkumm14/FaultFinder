from django.urls import path
from . import views
urlpatterns = [
    path('', views.projects, name="projects"),
    path('add-project/',views.add_project, name='add-project'),
    path('<int:pk>/dashboard/',views.dashboard,name='dashboard'),
    path('<int:pk>/dashboard/data', views.dashboard_data,name='dashboard-data')
]
