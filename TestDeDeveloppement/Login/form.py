from django.forms import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from Login.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError("Ce compte est inactif.", code='inactive')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', "password1", "password2"]