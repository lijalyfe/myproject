from django.urls import path
from . import views
from .views import product_detail
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<slug>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
