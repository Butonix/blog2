from django.contrib import messages
from django.shortcuts import render, get_object_or_404#function based views
from django.db.models import Q
from example.config import pagination
from .forms import PostForm

# Create your views here.

from .models import Post, Category

def post_list(request):
    template = 'blog/post_list.html'
    object_list = Post.objects.filter(status='Published')

    pages = pagination(request, object_list, num=1)

    context = {
        'items': pages[0],
        'page_range': pages[1],
    }
    return render(request, template, context)

def post_detail(request, slug):#function based  detail view, with slug that comes  from url
    template = 'blog/post_detail.html'#template path for r'^blog-detail/(?P<slug>[-\w]+)/$', post_detail, name="blog_detail

    post = get_object_or_404(Post, slug=slug) #varialbe names post, that gets slug

    context = {
    'post': post, #How we get our post data into out template post_detail.html
    }
    return render(request, template, context)#returns post

def category_detail(request, slug):
    template = 'blog/category_detail.html'#template path for r'^category-detail/(?P<slug>[-\w]+)/$', category_detail, name="category_detail"

    category = get_object_or_404(Category, slug=slug)#pass in the slug to find out which category
    post = Post.objects.filter(category=category, status='Published')#show all published posts

    context = {
    'category': category,
    'post': post,
    }
    return render(request, template, context)

def search(request):
    template = 'blog/post_list.html'

    query = request.GET.get('q')

    if query:
        results = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    else:
        results = Post.objects.filter(status="Published")

    pages = pagination(request, results, num=1)

    context = {
        'items': pages[0],
        'page_range': pages[1],
        'query': query,
    }
    return render(request, template, context)

def new_post(request):
    template = 'blog/new_post.html'
    form = PostForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Blog Post Was Successfully Saved')

    except Exception as e:
        form = PostForm()
        messages.warning(request, "Blog Post Failed To Save. Error: {}".format(e))

    context = {
        'form': form,
    }

    return render(request, template, context)

def post_list_admin(request):
    template = 'blog/post_list_admin.html'

    post = Post.objects.all()

    pages = pagination(request, post, 5)

    context = {
        'items': pages[0],
        'page_range': pages[1]
    }
    return render(request, template, context)


def edit_post(request, pk):
    template = 'blog/new_post.html'
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Your Blog Post Was Successfully Updated")

        except Exception as e:
            messages.warning(request, 'Your Post Was Not Saved Due To An Error: {}'.format(e))

    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)

def delete_post(request, pk):
    template = 'blog/new_post.html'

    post = get_object_or_404(Post, pk=pk)

    try:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            post.delete()
            messages.success(request, 'You have successfully deleted the post')
        else:
            form = PostForm(instance=post)
    except Exception as e:
        messages.warning(request, 'The post could not be deleted. Error {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)
