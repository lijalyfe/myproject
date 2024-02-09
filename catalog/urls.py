from django.urls import path
from .views import ProductDetailView
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    HomeView,
)

urlpatterns = [
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('homelist/', HomeView.as_view(), name='home_list'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<slug>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
