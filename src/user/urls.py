from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('sigin/', views.sigin, name='sigin'),
]
