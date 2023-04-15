from django.contrib.auth.models import User

from .models import Todo
from django.forms import ModelForm


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['description']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']