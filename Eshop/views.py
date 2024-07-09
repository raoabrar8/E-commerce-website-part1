from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Category, Product
from .forms import CategoryForm, ProductForm
# Create your views here.


def is_admin(user):
    return user.is_staff
# Admin Interface Views

@user_passes_test(is_admin)
def admin_dashboard(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'Admin/admin_dashboard.html', {'categories':categories, 'products':products})


@user_passes_test(is_admin)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
        
    else:
        form = CategoryForm()
    return render(request, 'Admin/add_category.html', {'form':form})

@user_passes_test(is_admin)
def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
        
    else:
        form = CategoryForm()
    return render(request, 'Admin/update_category.html', {'form':form})


@user_passes_test(is_admin)
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('admin_dashboard')

@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
        
    else:
        form = ProductForm()
        
    return render(request, 'Admin/add_product.html', {'form':form})

@user_passes_test(is_admin)
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
        
    else:
        form = ProductForm()
    return render(request, 'Admin/add_product.html', {'form':form})


@user_passes_test(is_admin)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('admin_dashboard')


# User Interface Views


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'User/category_list.html', {'categories':categories})

def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'User/product_list.html', {'category':category, 'products':products})


