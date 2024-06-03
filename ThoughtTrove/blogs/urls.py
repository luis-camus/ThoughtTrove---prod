from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_blog),
    path('<int:blog_id>/', views.view_blog),
    path('delete/<int:blog_id>', views.delete_blog)
]