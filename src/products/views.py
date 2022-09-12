from itertools import product
from unicodedata import category
from django import views
from django.http import  HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import  DetailView,UpdateView
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from .forms import UserForm,CodeForm,CreateProductForm,CreateProductLGForm,ImageForm,CommentForm,CommentForm_lg,MessageForm
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Avg,Sum,Avg,Count
# Create your views here.






class Base(DetailView):
    def get(self, request):
        prod = Product.objects.all().order_by('-created_date')[:8]
        lg = LegalProduct.objects.all().order_by('-created_date')[:8]
        user = request.user
        context={
            'prod':prod,
            'lg':lg
        }
        return render(request, 'shop/index.html',context)
#---------------
class SeeProductUser(View):    
    def get(self,request,user_id):
        user = User.objects.get(id = user_id)
        prod = Product.objects.filter(owner = user).order_by('-created_date')
        paginator = Paginator(prod,16)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'prod':prod,
        }
        return render(request, 'users/all_product_user.html',context)

class SeeProductUserLg(View):    
    def get(self,request,user_id):
        user = User.objects.get(id = user_id)
        prod = LegalProduct.objects.filter(owner = user).order_by('-created_date')
        paginator = Paginator(prod,16)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'prod':prod,
        }
        return render(request, 'users/all_product_user_lg.html',context)
#---------------

#---------------
class SeeProduct(View):
    def get(self, request): 
        search_query = request.GET.get('search','')
        if search_query:
            product = Product.objects.filter(Q(title__icontains=search_query)|Q(description__icontains=search_query))
        else:
            product = Product.objects.all().order_by('-created_date')


        category = Category.objects.all()
        sub = SubCategory.objects.all()
        paginator = Paginator(product,16)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'prod':product,
            'category':category,
            'sub':sub,
            'page_obj':page_obj
        }
        return render(request, 'shop/all_product.html',context)
class SeeProductLg(View):
    def get(self, request):  
        search_query = request.GET.get('search','')
        if search_query:
            product = LegalProduct.objects.filter(Q(title__icontains=search_query)|Q(description__icontains=search_query))
        else:
            product = LegalProduct.objects.all().order_by('-created_date')  
        category = CategoryLegal.objects.all()
        sub = SubCategoryLegal.objects.all()
        paginator = Paginator(product,16)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'prod':product,
            'category':category,
            'sub':sub,
            'page_obj':page_obj
        }
        return render(request, 'shop/all_product_lg.html',context)



        
#---------------

#---------------
class CategoryProductView(View):
    
    def get(self, request,category_slug,*args, **kwargs):
        cat =  SubCategory.objects.get(slug = category_slug)
        prod = Product.objects.filter(category_sub =  cat )
        category = Category.objects.all()
        sub = SubCategory.objects.all()
        paginator = Paginator(prod,16)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'cat':cat,
            'prod':prod,
            'category':category,
            'sub':sub,
            'page_obj':page_obj,
        }
        return render(request, 'shop/category.html',context)
class CategoryProductLgView(View):
    
    def get(self, request,category_slug,*args, **kwargs):
        cat =  SubCategoryLegal.objects.get(slug = category_slug)
        prod = LegalProduct.objects.filter(category_sub =  cat )
        category = CategoryLegal.objects.all()
        sub = SubCategory.objects.all()
        paginator = Paginator(prod,16)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'cat':cat,
            'prod':prod,
            'category':category,
            'sub':sub,
            'page_obj':page_obj,
        }
        return render(request, 'shop/category_lg.html',context)
#---------------
#---------------


def product_detail(request, product_slug):
    """ Вывод информации о конкретном товаре """

    product = get_object_or_404(Product, slug=product_slug)
    comments = ProductComment.objects.filter(product=product).aggregate(
        total_comments=Count("product"),
    )
    reviews = ProductComment.objects.filter(product=product).order_by('-date_created')
    lastprod = Product.objects.filter(owner = product.owner).order_by('-created_date')[:4]


    paginator = Paginator(reviews,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        if request.user.is_authenticated == False:
            return redirect('base')
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.product = product
            new_comment.save()
            return HttpResponseRedirect(request.path)
        else:
            pass
    else:
        form = CommentForm()
    context = {
        'product': product,
        'comments': comments,
        'reviews': reviews,
        'lastprod':lastprod,
        'page_obj':page_obj,
        'form':form,
    }

    return render(request, "shop/product_detail.html", context)

def product_detail_lg(request, product_slug):
    """ Вывод информации о конкретном товаре """

    product = get_object_or_404(LegalProduct, slug=product_slug)
    comments = ProductCommentLg.objects.filter(product=product).aggregate(
        total_comments=Count("product"),
    )
    reviews = ProductCommentLg.objects.filter(product=product).order_by('-date_created')
    lastprod = LegalProduct.objects.filter(owner = product.owner).order_by('-created_date')[:4]


    paginator = Paginator(reviews,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        if request.user.is_authenticated == False:
            return redirect('base')
        form = CommentForm_lg(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.product = product
            new_comment.save()
            return HttpResponseRedirect(request.path)
        else:
            pass
    else:
        form = CommentForm_lg()
    context = {
        'product': product,
        'comments': comments,
        'reviews': reviews,
        'lastprod':lastprod,
        'page_obj':page_obj,
        'form':form,
    }

    return render(request, "shop/product_detail_lg.html", context)

#---------------


class ProfileDetail(DetailView):
    def get(self,request,user_id):
        user = User.objects.get(id = user_id)
        prod = Product.objects.filter(owner = user).order_by('-created_date')[:4]
        profile = user.profile
        form = CodeForm(instance=profile)
        form2 = ImageForm(instance=profile)
        profile = user.profile
        context={
                'user':user,
                'form2':form2,
                'profile':profile,
                'product':prod,
                'form':form,
        }
        return render(request, 'users/profile_detail.html',context)

    def post(self,request,user_id):
        user = User.objects.get(id = user_id) 
        if user != request.user:
                return redirect('base')

        profile = user.profile
        form = CodeForm(request.POST,instance=profile)
        if form.is_valid():
            new_code = form.save()
            return redirect('profile_detail',user.id)
        return redirect('profile_detail',user.id)


class SendEmailView(View):
    def get(self,request,user_id):
        user = get_object_or_404(User,id = user_id) 
        if user != request.user:
            return redirect('base')
        form = MessageForm()
        context={
                'user':user,
                'form':form,
        }
        return render(request, 'users/create_message.html',context)

    def post(self,request,user_id):
        user = User.objects.get(id = user_id) 
        if user != request.user:
                return redirect('base')
        form = MessageForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = user
            new.save()
            return redirect('profile_detail',user.id)
        return redirect('profile_detail',user.id)
        




class EditImageView(View):
    def post(self,request,user_id):
        user = get_object_or_404(User,id = user_id) 
        if user != request.user:
            return redirect('base')
        profile = user.profile
        form = ImageForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail',user.id)
        return redirect('profile_detail',user.id)



class EditPasswordView(View):
    def post(self,request,user_id):
        user = get_object_or_404(User,id = user_id)  
        if user != request.user:
            return redirect('base')
        password_new = request.POST.get('password2')
        user.set_password(password_new)
        user.save()
        user.profile.save()
        messages.add_message(request, messages.SUCCESS,
                                 'You have successfully changed your password')
        return redirect('login')








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

#---------------

class DeleteView(View):
    def get(self, request,product_slug):
        user = request.user
        prod = Product.objects.get(slug =  product_slug )
        if user.is_authenticated == False:
            return redirect('base')
        if user != prod.owner:
            return redirect('base')
        prod.delete()
        return redirect('profile_detail',user.id)
class DeleteLgView(View):
    def get(self, request,product_slug):
        user = request.user
        prod = LegalProduct.objects.get(slug =  product_slug )
        if user.is_authenticated == False:
            return redirect('base')
        if user != prod.owner:
            return redirect('base')
        prod.delete()
        return redirect('profile_detail',user.id)


#---------------
class Reg(DetailView):
    def get(self, request):
        form=UserForm()
        form2=ImageForm()
        if request.user.is_authenticated:
            return redirect(to='base')
        return render(request, 'users/register.html',{
            'form':form,
            'form2':form2
        })

    def post(self,request,*args, **kwargs):
        form = UserForm(request.POST)
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
            profile = newuser.profile
            form2 = ImageForm(request.POST, request.FILES,instance=profile)
            if form2.is_valid():
                form2.save()
                messages.success(request, ('Your profile was successfully created!'))
                return redirect('login')
        return render(request, 'users/register.html',{
            'form':form,
        })

class Login(DetailView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(to='base')
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('base')
        else:
            messages.info(request,'Login or password is not correct....')
            return render(request, 'users/login.html')




def logoutUser(request):
    logout(request)
    return redirect('base')



#---------------
class CreateProduct(View):
    def get(self,request,user_id):
        user = User.objects.get(id = user_id) 
        form = CreateProductForm()
        if user != request.user:
                return redirect('base')
        context={
                'user':user,
                'form':form,
        }
        return render(request,'shop/create_product.html',context)

    def post(self,request,user_id):
        user = User.objects.get(id = user_id) 
        if user != request.user:
                return redirect('base')
        if user.profile.check_code == False:
                return redirect('base') 
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.owner = user
            new_product.slug= slugify(new_product.title)
            new_product.save()
            return redirect('profile_detail',user.id)
        context={
                'user':user,
                'form':form,
        }
        return render(request,'product/create_product.html',context)
class CreateLgProduct(View):
    def get(self,request,user_id):
        user = User.objects.get(id = user_id) 
        form = CreateProductLGForm()
        if user != request.user:
                return redirect('base')
        context={
                'user':user,
                'form':form,
        }
        return render(request,'shop/create_product_lg.html',context)

    def post(self,request,user_id):
        user = User.objects.get(id = user_id) 
        if user != request.user:
                return redirect('base')
        if user.profile.check_code == False:
                return redirect('base') 
        form = CreateProductLGForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.owner = user
            new_product.slug= slugify(new_product.title)
            new_product.save()
            return redirect('profile_detail',user.id)
        context={
                'user':user,
                'form':form,
        }
        return render(request,'product/create_product_lg.html',context)
#---------------
#---------------
class EditView(UpdateView):
    def get(self,request,product_slug):
        user = request.user
        prod = Product.objects.get(slug =  product_slug )
        form = CreateProductForm(instance=prod)
        if user.is_authenticated == False:
            return redirect('base')
        if user != prod.owner:
                return redirect('base')
        context={
                'user':user,
                'form':form,
                'prod':prod 
        }
        return render(request,'shop/edit_product.html',context)

    def post(self,request,product_slug):
        user = request.user
        prod = Product.objects.get(slug =  product_slug )
        form = CreateProductForm(request.POST, request.FILES,instance=prod)
        if user.is_authenticated == False:
            return redirect('base')
        if user != prod.owner:
                return redirect('base')
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.slug= slugify(new_product.title)
            new_product.save()
            return redirect('profile_detail',user.id)
        context={
                'user':user,
                'form':form,
        }
        return render(request,'shop/edit_product.html',context)
class EditLgView(UpdateView):
    def get(self,request,product_slug):
        user = request.user
        prod = LegalProduct.objects.get(slug =  product_slug )
        form = CreateProductLGForm(instance=prod)
        if user.is_authenticated == False:
            return redirect('base')
        if user != prod.owner:
                return redirect('base')
        context={
                'user':user,
                'form':form,
                'prod':prod 
        }
        return render(request,'shop/edit_product_lg.html',context)

    def post(self,request,product_slug):
        user = request.user
        prod = LegalProduct.objects.get(slug =  product_slug )
        form = CreateProductLGForm(request.POST, request.FILES,instance=prod)
        if user.is_authenticated == False:
            return redirect('base')
        if user != prod.owner:
                return redirect('base')
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.slug= slugify(new_product.title)
            new_product.save()
            return redirect('profile_detail',user.id)
        context={
                'user':user,
                'form':form,
        }
        return render(request,'shop/edit_product_lg.html',context)

#---------------


class ResetPassword(View):
    def get(self,request,user_id):
        user = User.objects.get(id = user_id) 
        if user != request.user:
                return redirect('base')
        context={
                'user':user,
        }
        return render(request, 'profile/reset_password.html',context)
    def post(self,request,user_id):
        user = User.objects.get(id = user_id) 
        if user != request.user:
                return redirect('base')
        password_new = request.POST.get('password2')
        user.set_password(password_new)
        user.save()
        user.profile.save()
        messages.add_message(request, messages.SUCCESS,
                                 'You have successfully changed your password')
        return redirect('login')







