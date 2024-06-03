from django.urls import path
from . import views
urlpatterns = [
    path('/create', views.create_account),
    path('/login', views.login),
    path('/logout', views.logout)
]