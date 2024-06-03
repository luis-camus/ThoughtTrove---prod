from django.db import models
from django.contrib.auth.models import User
# Create your models here.


    
class Blog(models.Model):
    blog_image = models.ImageField(null=True, blank=True, upload_to='blog_image/')
    title = models.CharField(max_length=100, null=False, blank=False)
    intro_text = models.CharField(null=False, blank=False, default="Stay curious, stay inspired, and let’s dive into the world of words together!")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 


