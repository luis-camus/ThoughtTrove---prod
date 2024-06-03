from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('register', views.register_page),
    path('login', views.login),
    path('main', views.main),
    path('profile', views.profile)
]
