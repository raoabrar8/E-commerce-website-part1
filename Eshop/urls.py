from django.urls import path
from . import views


urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/add_category/', views.add_category, name='add_category'),
    path('admin/update_category/<int:pk>/', views.update_category, name='update_category'),
    path('admin/delete_category/<int:pk>/', views.delete_category, name='delete_category'),
    path('admin/add_product/', views.add_product, name='add_product'),
    path('admin/update_prdoduct/<int:pk>', views.update_product, name='update_prodcut'),
    path('admin/delete_prodcut/<int:pk>', views.delete_product, name='delete_prodcut'),
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.product_list, name='product_list')
]
