from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import EmailField


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')
        field_classes = {
            'username': UsernameField,
            'email': EmailField,
        }
