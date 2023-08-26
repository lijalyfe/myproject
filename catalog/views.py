from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Blog
from .forms import BlogForm

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def product_detail(request, pk):
    product = Product.objects.all()
    return render(request, 'home.html', {'product': product})

class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/blog_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Blog.objects.filter(published=True).order_by('-created_at')

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_detail.html'

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_update.html'

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog_list')
