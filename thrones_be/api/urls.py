from django.urls import path
# from .views import ThroneList
from . import views


urlpatterns = [
    # path('', ThroneList.as_view()),

    path('', views.getRoutes),
    path('throne/', views.getThrone),
    path('thrones/', views.getBathrooms),
    path('throne/<str:pk>/', views.getBathroom),
    path('profiles/', views.getUsers),
    path('profile/', views.getUser),
    path('reviews/', views.getReviews),
]