from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('thrones/', views.getBathrooms),
    path('thrones/<str:pk>/', views.getBathroom),

]