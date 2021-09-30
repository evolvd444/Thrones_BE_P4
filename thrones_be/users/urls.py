from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name= "profiles"),
    path('login/', views.loginUser, name= "login"),
    path('logout/', views.logoutUser, name= "logout"),
    path('register/', views.registerUser, name= "register"),
    path('profile/<str:pk>/', views.userProfile, name= "user-profile"),
    path('account/', views.userAccount, name= "account"),
    path('edit-account/', views.editAccount, name= "edit-account"),
]