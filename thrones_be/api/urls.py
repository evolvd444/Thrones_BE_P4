from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('throne/', views.getThrone),
    path('thrones/', views.getBathrooms),
    path('thrones/<str:pk>/', views.getBathroom),
    path('profiles/', views.getUsers),
    path('profile/', views.getUser),
    path('reviews/', views.getReviews),
]