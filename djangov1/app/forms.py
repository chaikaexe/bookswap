from django import forms
from .models import BookSwap
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class BookSwapForm(ModelForm):
    class Meta:
        model = BookSwap
        fields = ["title", "author", "desc"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите автора'
            }),
            "desc": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email", )


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label='Bio', required=False)