from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from tasks.models import Task

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')


class TaskForm(forms.ModelForm):

  class Meta:
    model = Task
    fields = ['task_name', 'task_description', 'end_date']