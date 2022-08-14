from django.urls import path
from . import views

urlpatterns = [
    path('', views.Base.as_view(),name ='base'),
    path('all-product/', views.SeeProduct.as_view(),name ='all_product'),
    path('all-product-lg/', views.SeeLegal.as_view(),name ='all_product_lg'),
    path('login/', views.Login.as_view(),name ='login'),
    path('register/', views.Reg.as_view(),name ='reg'),
    path('logout/', views.logoutUser,name ='logout'),
    path("profile/<int:user_id>/",views.ProfileDetail.as_view(),name = "profile_detail"),
    path("profile/<int:user_id>/create-product/",views.CreateProduct.as_view(),name = "create_product"),
    path("profile/<int:user_id>/create-product-lg/",views.CreateProductLG.as_view(),name = "create_product_lg"),
    path("profile/<int:user_id>/reset-password/",views.ResetPassword.as_view(),name = "reset_password"),
    path("profile/<int:user_id>/code/",views.CodeupdateNew.as_view(),name = "code"),
    path("profile/<int:user_id>/cheking/",views.Checking.as_view(),name = "cheking")
]