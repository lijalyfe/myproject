from django.shortcuts import render, redirect
from .models import*
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .forms import BlogForm
from flask import Flask, render_template, request, redirect, url_for
from slugify import slugify

app = Flask(__name__)


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

@app.route('/articles/<slug>')
def view_article(slug):
    """Увеличение счетчика просмотров при открытии статьи"""
    article = Article.query.filter_by(slug=slug).first()
    if not article:
        abort(404)
    article.views += 1
    db.session.commit()
    return render_template('article.html', article=article)

@app.route('/articles')
def list_articles():
    """Вывод списка статей с положительным признаком публикации"""
    articles = Article.query.filter_by(published=True).all()
    return render_template('articles.html', articles=articles)

title = 'Статья об использовании Python в машинном обучении'
slug = slugify(title)
print(slug)  # 'statya-ob-ispolzovanii-python-v-mashinnom-obuchenii'

@app.route('/articles/<slug>/edit', methods=['GET', 'POST'])
def edit_article(slug):
    """Перенаправление пользователя после редактирования статьи"""
    article = Article.query.filter_by(slug=slug).first()
    if not article:
        abort(404)
    if request.method == 'POST':
        article.title = request.form['title']
        article.body = request.form['body']
        article.published = request.form.get('published', False)
        db.session.commit()
        return redirect(url_for('view_article', slug=article.slug))
    return render_template('edit_article.html', article=article)
