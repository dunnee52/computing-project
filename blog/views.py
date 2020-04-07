from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post 

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'blog/home.html', context)
    
class PostListView(ListView):
    model = Post
    template_name ='blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(CreateView):
    model = Post
    fields = ['author','title', 'content']
    
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
       
    

def about(request):
   return HttpResponse('<h1>Blog About</h1>')