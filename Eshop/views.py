from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Category, Product
from .forms import CategoryForm, ProductForm
# Create your views here.


def is_admin(user):
    return user.is_staff


@user_passes_test
def admin_dashboard(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'Admin/admin_dashboard.html', {'categories':categories, 'products':products})

