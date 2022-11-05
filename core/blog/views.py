from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

from django.views.generic import View

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        
        context = { 

        }
        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = { 
            'form': form

        }
        return render(request, 'create_post.html', context)

    def post(self, request, *args, **kwargs):
        

        if request.method=="POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get("title")
                content = form.cleaned_data.get("content") 
                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect("blog:home")
        context = { 
            'form': form

        }
        return render(request, 'create_post.html', context)

