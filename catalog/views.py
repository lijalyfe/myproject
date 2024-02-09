from django.shortcuts import render, redirect
from .models import Product, Blog
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.urls import reverse_lazy
from .forms import BlogForm
from slugify import slugify


def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Главная',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


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


title = 'Статья об использовании Python в машинном обучении'
slug = slugify(title)
print(slug)

