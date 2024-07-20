from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Category, Product
from .forms import CategoryForm, ProductForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def is_admin(user):
    return user.is_staff
# Admin Interface Views
@login_required
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
        form = CategoryForm(instance=category)
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
        form = ProductForm(instance = product)
    return render(request, 'Admin/update_product.html', {'form':form})


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


# cart views
def cart_details(request):
    cart =  request.session.get('cart', {})
    cart_item = []
    total_price = 0
    
    for item_id, item_data in cart.items():
        product = get_object_or_404(Product, id=item_id)
        quantity = item_data['quantity']
        total_price += product.price * quantity
        cart_item.append({
            'product':product,
            'quantity':quantity,
            'total_price': product.price * quantity
        })
        
    return render(request, 'User/cart_details.html', {'cart_item':cart_item, 'total_price':total_price})




# def cart_detail(request):
#     cart = request.session.get('cart',{})
#     cart_item = []
#     total_price = 0
    
    
#     for item_id, item_data in cart.item():
#         product = get_object_or_404(Product, id = item_id)
#         quantity = item_data['quantity']
#         total_price += quantity * product.price
        
#         cart_item.append({
#             'product': product,
#             'quantity': quantity,
#             'total_price': quantity * product.price
                
#         })
        
#     return render(request, 'User/cart_details.html', {'cart_item':cart_item, 'total_price':total_price})
        
        



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    # print(product)
    # print(cart)
    
    if str(product.id) in cart:
        cart[str(product.id)]['quantity'] += 1
    else:
        cart[str(product.id)] = {'quantity' : 1}
        
    request.session['cart'] = cart
    return redirect('cart_details')

# def add_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart = request.session.get('cart', {})
#     if str(product.id) in cart:
#         cart[str(product.id)]['quantity'] +=1
#     else:
#         cart[str(product.id)]+= {'quantity' : 1}
        
        
#     request.sesssion.get['cart'] = cart
    


    


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        
    return redirect('cart_details')
          
          
# def remove_from_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart = request.session.get('cart', {})
    
#     if str(product_id) in cart:
#         del cart[str(product_id)]
#         request.session['cart'] = cart

