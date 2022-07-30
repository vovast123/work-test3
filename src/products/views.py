from django.views.generic import  DetailView
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.http import Http404,HttpResponseRedirect
from django.contrib import messages
from .forms import UserForm,ProfileForm
# Create your views here.
class Base(DetailView):
    def get(self, request):
        user = request.user
        prod = Product.objects.all().order_by('-created_date')
        context={
            'prod':prod
        }
        return render(request, 'base.html',context)


class Log(DetailView):
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
        if form.is_valid():
            newuser = form.save(commit=False)
            newuser.save()
            form2 = ProfileForm(request.POST, instance=newuser.profile)
            if form2.is_valid():
                profile =  form2.save(commit=False)
                profile.save()
                messages.success(request, ('Your profile was successfully created!'))
                return redirect('login')
        return render(request, 'reg.html',{
            'form':form,
            'form2':form2,
        })


def logoutUser(request):
    logout(request)
    return redirect('login')