from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Write your username',
            'class': 'input-form  username-class'
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Write your Email',
            'class': 'input-form email-class'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Write your password',
            'class': 'input-form password-class password-secret'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Repeat your password',
            'class': 'input-form password-class password-secret-repeat'
        }
    ))

    # profile = forms.ImageField(widget=forms.FileInput(
    #   attrs={
    #      'placeholder': 'Repeat your password',
    #       'class': 'input-form password-class password-secret-repeat'
    #    }
    # ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 2, 'placeholder': '¿Qué está pasando?'}),
                              required=True)

    class Meta:
        model = Post
        fields = ['content']
