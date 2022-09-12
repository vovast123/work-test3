from dataclasses import fields
from pyexpat import model
from xml.dom import ValidationErr
from .models import User,Profile,Product,LegalProduct,ProductComment,ProductCommentLg,Message
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class UserForm(UserCreationForm):      
    class Meta:
        model = User
        fields = ('username', 'last_name','password1','password2',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('describe',)
        widgets = {
            "describe": forms.Textarea(attrs={"cols": "45", "rows": "8", "style": "height: 99px;"})
        }

class CodeForm(forms.ModelForm):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp'}))
    class Meta:
        model = Profile
        fields = ('code',)



class CreateProductForm(forms.ModelForm):
  
    
    class Meta:
        model = Product
        fields = ('title','picture','category_sub','description','contact','phone','price')




class CreateProductLGForm(forms.ModelForm):
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