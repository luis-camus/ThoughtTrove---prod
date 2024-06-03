from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect("/main")
        else:
            pass
    form = BlogForm()
    return render(request, 'main/writeblog.html', {'form': form})

# def view_blog(request, blog_id):
#     return render(request, 'main/blog.html')

def view_blog(request, blog_id):
    blog = Blog.objects.filter(id=blog_id)
    author = User.objects.filter(id=blog[0].author_id)
    title = blog[0].title
    is_blog_owned_by_user = blog[0].author_id == request.user.id
    print(is_blog_owned_by_user)
    return render(request, 'main/blog.html', {'blog': blog, 'author': author[0], 'title': title, 'owned': is_blog_owned_by_user})

def delete_blog(request, blog_id):
    blog_to_delete = get_object_or_404(Blog, pk=blog_id)
    blog_to_delete.delete()
    blogs = Blog.objects.filter(author_id=request.user.id)
    render(request, 'main/profilepage.html', {'blogs': blogs})
    return redirect('/profile')