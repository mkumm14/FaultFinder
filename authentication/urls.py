from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login', LoginView.as_view(form_class=LoginForm,template_name="authentication/login.html"), name="login"),
    path('register', views.register_view, name="register"),
    path('logout', views.logout_view, name="logout"),
    path('profile', views.profile_view, name="user-profile"),
    path('user/<int:pk>/edit',views.edit_user, name="edit-user")
]
