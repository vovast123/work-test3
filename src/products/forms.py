from dataclasses import fields
from xml.dom import ValidationErr
from .models import User,Profile,Product,LegalProduct
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

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

class CodeForm(forms.ModelForm):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'inputt'}))
    class Meta:
        model = Profile
        fields = ('code',)

class CreateProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp-txt mb-2'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    discount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    
    
    class Meta:
        model = Product
        fields = ('picture','category','category_sub','title','description','price','discount')



class CreateProductLGForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp-txt mb-2'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    discount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    
    
    class Meta:
        model = LegalProduct
        fields = ('picture','category','category_sub','title','description','phone','description_add','price','discount')

