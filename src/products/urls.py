from django.urls import path
from . import views
urlpatterns = [
    path('', views.Base.as_view(),name ='base'),
    path('22', views.twtw.as_view(),name ='twtw'),
    path('legal-product/', views.BaseLg.as_view(),name ='legal'),
    path('category/<slug:category_slug>/', views.CategoryProductView.as_view(),name ='category'),
    path('detail/<slug:product_slug>/', views.product_detail,name ='detail'),
    path('detail-lg/<slug:product_slug>/', views.product_detail_lg,name ='detail_lg'),
    path('detail/<slug:product_slug>/edit/', views.EditView.as_view(),name ='edit'),
    path('detail-lg/<slug:product_slug>/edit/', views.EditLgView.as_view(),name ='edit_lg'),
    path('detail/<slug:product_slug>/delete/', views.DeleteView.as_view(),name ='delete'),
    path('detail-lg/<slug:product_slug>/delete/', views.DeleteLgView.as_view(),name ='delete_lg'),
    path('category-lg/<slug:category_slug>/', views.CategoryProductLgView.as_view(),name ='category_lg'),
    path('all-product/', views.SeeProduct.as_view(),name ='all_product'),
    path('all-product-lg/', views.SeeLegal.as_view(),name ='all_product_lg'),
    path('login/', views.Login.as_view(),name ='login'),
    path('register/', views.Reg.as_view(),name ='reg'),
    path('logout/', views.logoutUser,name ='logout'),
    path("profile/<int:user_id>/",views.ProfileDetail.as_view(),name = "profile_detail"),
    path("profile-lg/<int:user_id>/",views.ProfileDetailLg.as_view(),name = "profile_detail_lg"),
    path("profile/<int:user_id>/create-product/",views.CreateProduct.as_view(),name = "create_product"),
    path("profile/<int:user_id>/create-product-lg/",views.CreateProductLG.as_view(),name = "create_product_lg"),
    path("profile/<int:user_id>/reset-password/",views.ResetPassword.as_view(),name = "reset_password"),
    path("profile/<int:user_id>/code/",views.CodeupdateNew.as_view(),name = "code"),
    path("profile/<int:user_id>/cheking/",views.Checking.as_view(),name = "cheking")
]