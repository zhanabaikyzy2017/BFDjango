from django.contrib import admin
from .models import Product,Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =('id','name','price','count','category')
    search_fields =('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

