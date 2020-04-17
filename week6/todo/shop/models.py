from django.db import models
from auth_.models import MyUser
import datetime

class CategoryManager(models.Manager):
    def for_user(self,user):
        return self.filter(created_by = user)


class Category(models.Model):
    name = models.CharField(max_length=300)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    objects = CategoryManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    pass

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    objects = ProductManager()


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
