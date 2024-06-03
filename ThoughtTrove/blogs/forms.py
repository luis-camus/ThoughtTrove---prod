from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    blog_image = forms.ImageField(label='Featured Image', widget=forms.ClearableFileInput(attrs={
        'class': 'form-control'
    }))
    title = forms.CharField(label='Blog Title',max_length=60, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    intro_text = forms.CharField(label='Introduction Text', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    content = forms.CharField(label='Content', required=True, widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Blog
        fields = [
            'blog_image',
            'title',
            'intro_text',
            'content'
        ]