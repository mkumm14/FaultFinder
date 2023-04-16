from django import forms
from django.contrib.auth.models import User
from .models import Project
from datetime import date
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.exceptions import ValidationError


class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'end_date']
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        if end_date and end_date < date.today():
            raise ValidationError("End date can't be in the past.")
        return end_date
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Create Project'))

    def save(self, commit=True):
        instance = super(ProjectForm, self).save(commit=False)
        instance.owner = self.request.user
        instance.updated_by = self.request.user
        if commit:
            instance.save()
            instance.users.add(self.request.user)
        return instance