from dataclasses import fields
from xml.dom import ValidationErr
from .models import User,Profile,Product,LegalProduct,ProductComment,ProductCommentLg
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

class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture',)


class CodeForm(forms.ModelForm):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp'}))
    class Meta:
        model = Profile
        fields = ('code',)

class CreateProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    picture = forms.ImageField()
    
    
    class Meta:
        model = Product
        fields = ('picture','category_sub','contact','phone','title','description','price')




class CreateProductLGForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    description_add = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'inp mb-2'}))

    
    
    class Meta:
        model = LegalProduct
        fields = ('picture','category_sub','title','contact','description','phone','description_add','price')



 #   star = forms.ModelChoiceField(
#        queryset=RaitingStar.objects.all(),widget=forms.RadioSelect(),empty_label=None
 #   )

class CommentForm(forms.ModelForm):
    
    

    class Meta:
        model = ProductComment
        fields = ("rating", "text",)
        labels = {
            "rating": "Рейтинг",
        }
        widgets = {
            "text": forms.Textarea(attrs={"cols": "45", "rows": "8", "style": "height: 99px;"})
        }

class CommentForm_lg(forms.ModelForm):
    
    

    class Meta:
        model = ProductCommentLg
        fields = ("rating", "text",)
        labels = {
            "rating": "Рейтинг",
        }
        widgets = {
            "text": forms.Textarea(attrs={"cols": "45", "rows": "8", "style": "height: 99px;"})
        }