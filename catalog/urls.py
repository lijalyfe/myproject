from django.urls import path
from . import views
from .views import product_detail

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]
