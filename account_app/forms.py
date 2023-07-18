from django import forms
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "input--style-4", 'placeholder': "username"}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={"class": "input--style-4", 'placeholder': "password"}))

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "input--style-4",
                "style": "max-width: 350px;"
            }),
            "password": forms.PasswordInput(attrs={
                "class": "input--style-4",
                "style": "max-width: 350px;"
            }),
            "email": forms.EmailInput(attrs={
                "class": "input--style-4",
                "style": "max-width: 350px;"
            })
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise ValidationError('this user already has exist', code='user_exist')

        return username


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')










