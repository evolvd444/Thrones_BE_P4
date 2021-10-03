from django.urls import path
from . import views


urlpatterns = [
    # path('api/', ThroneList.as_view()),dylan

    path('', views.getRoutes),
    path('throne/', views.getThrone),
    path('thrones/', views.getBathrooms),
    path('throne/<str:pk>/', views.getBathroom),
    path('profiles/', views.getUsers),
    path('profile/', views.getUser),
    path('reviews/', views.getReviews),
]