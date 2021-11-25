from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

class BlogListView(ListView): # for the main page
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):  # for detail view of the each post
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):  # for posting a new content 
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView): # for editing post
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView): # To delete the post
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")   