from django.db import models
from auth_.models import MyUser
import datetime
# from demo.utils.validators import validate_file_size, validate_extension

class CategoryManager(models.Manager):
    def for_user(self,user):
        return self.filter(created_by = user)


class BaseCategory(models.Model):
    name = models.CharField(max_length=300)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(BaseCategory):
    type = models.CharField(max_length=200, default='default')
    objects = CategoryManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    @classmethod
    def order(cls):
        return cls.objects.order_by('type')

class ProductManager(models.Manager):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return super(StatusManager,self).get_queryset().filter(status=2) or super(StatusManager,self).get_queryset().filter(status=1)

class Product(models.Model):
    STATUSES = (
        (1,'in_warehouse'),
        (2,'in_store'),
        (3,'sold_out')
    )
    picture = models.ImageField(upload_to='product_pictures',null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    status = models.IntegerField(choices=STATUSES, default=2)

    objects = ProductManager()
    status_check = StatusManager()

    @property
    def information(self):
        return self.name + str(self.price)

    @classmethod
    def in_warehouse_count(cls):
        return cls.objects.filter(status=2).count()

    @classmethod
    def in_store_count(cls):
        return cls.objects.filter(status=1).count()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
