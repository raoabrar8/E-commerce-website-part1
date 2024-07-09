from django.urls import path
from . import views

urlpatterns = [
    path('myadmin/', views.admin_dashboard, name='admin_dashboard'),
    path('myadmin/category/add/', views.add_category, name='add_category'),
    path('myadmin/category/update/<int:pk>/', views.update_category, name='update_category'),
    path('myadmin/category/delete/<int:pk>/', views.delete_category, name='delete_category'),
    path('myadmin/product/add/', views.add_product, name='add_product'),
    path('myadmin/product/update/<int:pk>/', views.update_product, name='update_product'),
    path('myadmin/product/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.product_list, name='product_list'),
]
