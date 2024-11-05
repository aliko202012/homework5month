from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
    blog = Blog.objects.all()
    return render(request, 'index.html', locals())