# imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Profile

# Register form


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )

# Profile page edit form


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = [
            'user',
            'token',
            'verify',
        ]
        widgets = {'gender': forms.RadioSelect()}
        #label = {'pro_img': forms.FileInput(label='Upload profile picture')}
