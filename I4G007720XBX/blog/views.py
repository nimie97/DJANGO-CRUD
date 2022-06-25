from msilib.schema import CreateFolder
from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import Post 

class PostListView(ListView):
    model = Post

from django.views.generic.list import ListView
from .models import Post 

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

from django.views.generic.list import ListView
from .models import Post 

class PostDetailView(Detail.view):
    model = Post

from django.views.generic.list import ListView
from .models import Post 

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

from django.views.generic.list import ListView
from .models import Post 

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
