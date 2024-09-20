from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from Login.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', "password1", "password2"]