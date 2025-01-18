from django.shortcuts import render, get_object_or_404
from .models import Product, Cart, CartItem, Customer, Order, Category, Offer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    offers = Offer.objects.all()  # Fetch all offers
    return render(request, 'home.html', {'categories': categories, 'products': products, 'offers': offers})
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
def cart(request):
    items = Cart.objects.all()
    return render(request, 'cart.html', {'items': items})
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('home')
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')
@login_required
def view_cart(request):
    items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in items)
    return render(request, 'cart.html', {'items': items, 'total_price': total_price})
@login_required
def place_order(request):
    customer = Customer.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    order = Order.objects.create(customer=customer, total_price=total_price)
    order.cart_items.set(cart_items)
    cart_items.delete()  # Clear the cart after placing the order
    return redirect('order_success')
@login_required
def customer_profile(request):
    customer = Customer.objects.get(user=request.user)
    return render(request, 'customer_profile.html', {'customer': customer})
@login_required
def order_list(request):
    customer = request.user.customer
    orders = Order.objects.filter(customer=customer)
    return render(request, 'order_list.html', {'orders': orders})
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer__user=request.user)
    return render(request, 'order_detail.html', {'order': order})
@login_required
def order_success(request):
    return render(request, 'order_success.html')
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {'category': category, 'products': products})
def search(request):
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
    else:
        results = Product.objects.none()  
    return render(request, 'search_results.html', {'results': results, 'query': query})
def offers_view(request):
    offers = Offer.objects.all()
    return render(request, 'offers.html', {'offers': offers})

def products_with_offer(request, offer_id):
    offer = Offer.objects.get(pk=offer_id)
    products = offer.products.all()  # Use the custom related_name
    return render(request, 'products_with_offer.html', {'offer': offer, 'products': products})
