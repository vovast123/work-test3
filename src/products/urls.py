from django.urls import path
from . import views

urlpatterns = [
    path('', views.Base.as_view(),name ='base'),
    path('login/', views.Log.as_view(),name ='login'),
    path('register/', views.Reg.as_view(),name ='reg'),
    path('logout/', views.logoutUser,name ='logout'),
]