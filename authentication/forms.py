from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

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