from django.contrib import admin
from .models import Product, Category, SubCategory, Newsletter

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Newsletter)
