from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field,HTML
from crispy_bootstrap5.bootstrap5 import FloatingField

class LoginForm(AuthenticationForm):
       username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username','type': 'text', 'placeholder':'Enter username...', 'required': True}), 
                                   error_messages={'required': 'Please enter your username.'})
       password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password','placeholder':'Enter password...', 'required': True}),
                                   error_messages={'required': 'Please enter your password.'})

       error_messages = {
              'invalid_login': _(
              "Please enter a correct %(username)s and password. Note that both "
              "fields may be case-sensitive."
              ),
              'inactive': _("This account is inactive."),
              'invalid_credentials': _("Invalid login credentials. Please try again."),
       }

       def clean(self):
              username = self.cleaned_data.get('username')
              password = self.cleaned_data.get('password')

              if username and password:
                     self.user_cache = authenticate(username=username, password=password)
                     if self.user_cache is None:
                            raise forms.ValidationError(
                            self.error_messages['invalid_credentials'],
                            code='invalid_credentials',
                            )
                     else:
                            self.confirm_login_allowed(self.user_cache)

              return self.cleaned_data
       




class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    email = forms.EmailField(max_length=100, label='Email')

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.attrs={
          'novalidate': ''
    }
    helper.form_id = 'register-form'
    helper.form_novalidate=True
    helper.layout = Layout(
        Div(
            FloatingField('username', placeholder='Username'),
            css_class='form-floating mb-3'
        ),
        Div(
            Div(
                FloatingField('first_name', placeholder='First Name'),
                css_class='col-md-6 form-floating mb-3'
            ),
            Div(
                FloatingField('last_name', placeholder='Last Name'),
                css_class='col-md-6 form-floating mb-3'
            ),
            css_class='row'
        ),
        Div(
            FloatingField('email', placeholder='Email'),
            css_class='form-floating mb-3'
        ),
        Div(
            Div(
                FloatingField('password1', placeholder='Password'),
                css_class='col-md-6 form-floating mb-3'
            ),
            Div(
                FloatingField('password2', placeholder='Confirm Password'),
                css_class='col-md-6 form-floating mb-3'
            ),
            css_class='row'
        )
    )

    helper.layout.append(
        HTML('<div class="mt-4 mb-0">'
             '<div class="d-grid">'
             '<button type="submit" class="btn btn-primary btn-block">Create Account</button>'
             '</div>'
             '</div>')
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
