from django.shortcuts import render
from .models import Blog

def index(request):
    """Render the home page."""
    return render(request, "index.html")

def blog_list(request):
    """List all blogs."""
    blogs = Blog.objects.all()
    return render(request, "blog_list.html", {"blogs": blogs})
