from django.urls import path
from . import views
urlpatterns = [
    path('', views.Base.as_view(),name ='base'),


    path('all-product/', views.SeeProduct.as_view(),name ='all_product'),
    path('all-legal-service/', views.SeeProductLg.as_view(),name ='all_product_lg'),


    path('category/<slug:category_slug>/', views.CategoryProductView.as_view(),name ='category'),
    path('category/legal-service/<slug:category_slug>/', views.CategoryProductLgView.as_view(),name ='category_lg'),


    path('detail/<slug:product_slug>/', views.product_detail,name ='detail'),
    path('detail/legal-service/<slug:product_slug>/', views.product_detail_lg,name ='detail_lg'),



    path("profile/<int:user_id>/",views.ProfileDetail.as_view(),name = "profile_detail"),


    path("profile/<int:user_id>/product/",views.SeeProductUser.as_view(),name = "all_product_user"),
    path("profile/<int:user_id>/legal-service/",views.SeeProductUserLg.as_view(),name = "all_product_user_lg"),


    path("profile/<int:user_id>/cheking/",views.Checking.as_view(),name = "cheking"),
    path("profile/<int:user_id>/edit-image/",views.EditImageView.as_view(),name = "edit_image"),
    path("profile/<int:user_id>/reset-password/",views.EditPasswordView.as_view(),name = "reset_password"),
    path("profile/<int:user_id>/send-message/",views.SendEmailView.as_view(),name = "send_message"),



    path('register/', views.Reg.as_view(),name ='reg'),
    path('login/', views.Login.as_view(),name ='login'),
    path('logout/', views.logoutUser,name ='logout'),


    path("profile/<int:user_id>/create-product/",views.CreateProduct.as_view(),name = "create_product"),
    path("profile/<int:user_id>/create-product/lg/",views.CreateLgProduct.as_view(),name = "create_product_lg"),


    path('detail/<slug:product_slug>/edit/', views.EditView.as_view(),name ='edit'),
    path('detail/<slug:product_slug>/edit-lg/', views.EditLgView.as_view(),name ='edit_lg'),


    path('detail/<slug:product_slug>/delete/', views.DeleteView.as_view(),name ='delete'),
    path('detail/<slug:product_slug>/delete-lg/', views.DeleteLgView.as_view(),name ='delete_lg'),



    path("profile/<int:user_id>/reset-password/",views.ResetPassword.as_view(),name = "reset_password"),

]