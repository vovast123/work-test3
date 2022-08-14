from itertools import product
from django.forms import SlugField
from django.http import Http404
from django.views import View
from django.views.generic import  DetailView,UpdateView
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserForm,ProfileForm,CodeForm,CreateProductForm,CreateProductLGForm
from django.utils.text import slugify
# Create your views here.
class Base(DetailView):
    def get(self, request):
        user = request.user
        prod = Product.objects.all().order_by('-created_date')
        context={
            'prod':prod
        }
        return render(request, 'base.html',context)

class SeeProduct(View):
    def get(self, request):    
        product = Product.objects.all().order_by('-created_date')
        context={
            'product':product
        }
        return render(request, 'product_all.html',context)

class SeeLegal(View):
    def get(self, request):    
        product = LegalProduct.objects.all().order_by('-created_date')
        context={
            'product':product
        }
        return render(request, 'product_all.html',context)



class Login(DetailView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(to='base')
        return render(request, 'log.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('base')
        else:
            messages.info(request,'Login or password is not correct....')
            return render(request, 'log.html')



class Reg(DetailView):
    def get(self, request):
        form=UserForm()
        form2 = ProfileForm()

        if request.user.is_authenticated:
            return redirect(to='base')
        return render(request, 'reg.html',{
            'form':form,
            'form2':form2,
        })

    def post(self,request,*args, **kwargs):
        form = UserForm(request.POST)
        form2 = ProfileForm(request.POST)
        if form.is_valid():    
            newuser = form.save(commit=False)
            if User.objects.filter(username=newuser.username).exists():
                messages.add_message(request, messages.ERROR,
                                 'This nickname is already taken')
                return redirect('reg')
            if len(newuser.password) < 8:
                messages.add_message(request, messages.ERROR,
                    'Password must be longer than 8 characters')
                return redirect('reg')
            if newuser.last_name == '':
                messages.add_message(request, messages.ERROR,
                                 'Enter first and last name')
                return redirect('reg')

            newuser.save()
            form2 = ProfileForm(request.POST, instance=newuser.profile)
            if form2.is_valid():
                profile =  form2.save(commit=False)
                profile.save()
                messages.success(request, ('Your profile was successfully created!'))
                return redirect('login')
        return render(request, 'reg.html',{
            'form':form,
            'form2':form2
        })


def logoutUser(request):
    logout(request)
    return redirect('login')



class ProfileDetail(DetailView):
    def get(self,request,user_id):
        user = User.objects.get(id = user_id)
        if user.is_authenticated == False:
            if user != request.user:
                return redirect('base')
        profile = user.profile
        context={
                'user':user,
                'profile':profile,
        }
        return render(request, 'user_detail.html',context)

class Checking(DetailView):
    def get(self,request,user_id):
        user = User.objects.get(id = user_id)
        if user.is_authenticated == False:
            if user != request.user:
                return redirect('base')
        if user.profile.check_code_fail == True :
            user.profile.check_code_fail = False 
        user.profile.for_checking = True
        user.save() 
        return redirect('profile_detail',user.id)

class CodeupdateNew(View):
    def get(self,request,user_id):
        
        user = User.objects.get(id = user_id) 
        if user.is_authenticated == False:
            if user != request.user:
                return redirect('base')
 
        profile = user.profile
        form = CodeForm(instance=profile)
        context={
                'user':user,
                'profile':profile,
                'form':form,
        }
        return render(request, 'code.html',context)
    def post(self,request,user_id):
        user = User.objects.get(id = user_id) 
        if user.is_authenticated == False:
            if user != request.user:
                return redirect('base')

        profile = user.profile
        form = CodeForm(request.POST,instance=profile)
        if form.is_valid():
            new_code = form.save()
            return redirect('profile_detail',user.id)
        return render(request, 'code.html')

        
class ResetPassword(View):
    def get(self,request,user_id):
        user = User.objects.get(id = user_id) 
        if user.is_authenticated == False:
            if user != request.user:
                return redirect('base')
        context={
                'user':user,
        }
        return render(request, 'reset_password.html',context)
    def post(self,request,user_id):
        user = User.objects.get(id = user_id) 
        if user.is_authenticated == False:
            if user != request.user:
                return redirect('base')
        password_new = request.POST.get('password2')
        user.set_password(password_new)
        user.save()
        user.profile.save()
        messages.add_message(request, messages.SUCCESS,
                                 'You have successfully changed your password')
        return redirect('login')


class CreateProduct(View):
    def get(self,request,user_id):
        user = User.objects.get(id = user_id) 
        form = CreateProductForm()
        if user.is_authenticated == False:
            if user != request.user:
                return redirect('base')
        context={
                'user':user,
                'form':form,
        }
        return render(request,'create_product.html',context)

    def post(self,request,user_id):
        user = User.objects.get(id = user_id) 
        if user.is_authenticated == False:
            if user != request.user:
                return redirect('base')
        form = CreateProductForm(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.owner = user
            new_product.slug= slugify(new_product.title)
            new_product.save()
            return redirect('profile_detail',user.id)
        return render(request, 'create_product.html') 


class CreateProductLG(View):
    def get(self,request,user_id):
        user = User.objects.get(id = user_id) 
        form = CreateProductLGForm()
        if user.is_authenticated == False:
            if user != request.user:
                return redirect('base')
        context={
                'user':user,
                'form':form,
        }
        return render(request,'create_product_lg.html',context)

    def post(self,request,user_id):
        user = User.objects.get(id = user_id) 
        if user.is_authenticated == False:
            if user != request.user:
                return redirect('base')
            
        form = CreateProductLGForm(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.owner = user
            new_product.slug= slugify(new_product.title)
            new_product.save()
            return redirect('profile_detail',user.id)
        return render(request, 'create_product_lg.html') 

