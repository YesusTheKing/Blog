from django.shortcuts import render
from .models import Blog,BlogComment
from django.http import HttpResponse
# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    context = {'data':blogs}
    return render(request, "BlogPost/blogs.html",context=context)

def detail(request,blog_id):
    blogs = Blog.objects.filter(BlogId=blog_id)
    comments = BlogComment.objects.filter(BlogId=blog_id)
    context = {'data':blogs,'comments':comments}
    return render(request, "BlogPost/blog_detail.html",context=context)
