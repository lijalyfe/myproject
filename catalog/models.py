from django.db import models
from PIL import Image
from .models import Category

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

    # категория продукта
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # цена за покупку товара
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # дата создания записи о товаре
    created = models.DateTimeField(auto_now_add=True)
    # дата последнего изменения записи о товаре
    updated = models.DateTimeField(auto_now=True)

