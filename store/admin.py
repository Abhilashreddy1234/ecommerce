from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Customer, Order, Offer

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Offer)
