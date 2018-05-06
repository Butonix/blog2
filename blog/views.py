from django.shortcuts import render, get_object_or_404#function based views
from django.views.generic.list import ListView#class based view
from django.views.generic.detail import DetailView#classed based detail view
# Create your views here.

from .models import Post

class PostListView(ListView):#classed based view in django, that inherits

    model = Post#Now this class knows its getting data from the Post table

    def get_context_data(self, **kwargs):#gets the data from our table
        context = super(PostListView, self).get_context_data(**kwargs)
        return context#return context variable, that has PostListView from database

class PostDetailView(DetailView):#classed based detail view in django, that inherits

    model = Post

    def get_context_data(self, **kwargs):#gets the data from our table
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context#return context variable, that has PostDetailView from database

def post_list(request):#function based view that renders a page
    template = 'blog/post_list.html'#template that post_list
    object_list = Post.objects.filter(status='Published')#should render published posts only, in templates {% if obj.status == 'Published' %}

    context = {
    'object_list': object_list, #How we get our data list into out template post_list.html
    }
    return render(request, template, context)#returns request for all objects, and passed it too the template


def post_detail(request, slug):#function based  detail view, with slug that comes  from url
    template = 'blog/post_detail.html'#template path that post_detail.html

    post = get_object_or_404(Post, slug=slug) #varialbe names post, that gets slug

    context = {
    'post': post, #How we get our post data into out template post_detail.html
    }
    return render(request, template, context)#returns post
