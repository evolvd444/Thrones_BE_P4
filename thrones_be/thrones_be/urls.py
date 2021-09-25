from django.urls import path
from . import views


urlpatterns = [
    path('bathroom/<str:pk>/', views.bathroom, name="bathroom"),
    path('', views.bathrooms, name= "bathrooms"),
    path('create-throne', views.createThrone, name="create-throne"),
    path('update-throne/<str:pk>/', views.updateThrone, name= "update-throne"),
    path('delete-throne/<str:pk>/', views.deleteThrone, name= "delete-throne"),

]