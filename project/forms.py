from django import forms
from .models import Project

class addProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=('title','description','end_date')