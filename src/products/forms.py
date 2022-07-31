from xml.dom import ValidationErr
from .models import User,Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=150)
    def clean(self):
        new_name = self.cleaned_data['username']
    class Meta:
        model = User
        fields = ('username', 'last_name', 'email','password1','password2',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture',)