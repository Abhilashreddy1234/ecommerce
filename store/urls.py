from django.urls import path
from . import views
from . views import place_order

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('place-order/', place_order, name='place_order'),
    path('cart/', views.view_cart, name='cart'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('profile/', views.customer_profile, name='customer_profile'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order-success/', views.order_success, name='order_success'), 
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_products, name='category_products'),
    path('search/', views.search, name='search'),
    path('offers/', views.offers_view, name='offers'),
    path('offers/<int:offer_id>/products/', views.products_with_offer, name='products_with_offer'),
]
