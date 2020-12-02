from django.shortcuts import render
from .models import Blog
# Create your views here.


def home_blog(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/home_blog.html', {'blogs':blogs})