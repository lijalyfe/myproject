from django.db import models
from PIL import Image
from django.apps import apps
from datetime import datetime
from django.utils.text import slugify

class Category(models.Model):
    # наименование категории
    name = models.CharField(max_length=250)
    # описание категории
    description = models.TextField(blank=True)
    # добавленное поле
    created_at = models.DateTimeField(default=datetime.now, editable=False)

class Product(models.Model):
    # наименование продукта
    name = models.CharField(max_length=250)
    # описание продукта
    description = models.TextField(blank=True)
    # изображение продукта
    image = models.ImageField(upload_to='products/', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            with Image.open(self.image.path) as img:
                img.thumbnail((800, 800))
                img.save(self.image.path)

    def get_category_name(self):
        Category = apps.get_model(app_label='catalog', model_name='Category')
        return Category.objects.get(id=self.category.id).name

    # категория продукта
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # цена за покупку товара
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # дата создания записи о товаре
    created = models.DateTimeField(auto_now_add=True)
    # дата последнего изменения записи о товаре
    updated = models.DateTimeField(auto_now=True)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    preview = models.ImageField(upload_to='blog_previews/')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)