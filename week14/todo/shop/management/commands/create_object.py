from django.core.management.base import BaseCommand
from shop.models import Product, Category

class Command(BaseCommand):
    help='Create fake data for optional table'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of objects to create')
        # parser.add_argument('-p', '--product', type=str, help='Argument to create Product object')
        parser.add_argument('-n', '--name', type=str, help='Name od creating object')
        parser.add_argument('-c', '--category', type=int, help='Category id')
        parser.add_argument('-ifcat', '--ifcategory', action='store_true', help='Create Category instead of Product')


    def handle(self, *args, **kwargs):
        count = kwargs['count']
        ifcat = kwargs.get('ifcategory')
        name = kwargs.get('name')
        c = kwargs.get('category')


        if not name:
            name = 'dafault'
        if not c:
            c = 1

        for i in range(count):
            if ifcat:
                cat = Category.objects.create(name=f'{name}_category{i}',
                                              type = 'new')
                self.stdout.write(f'Category{cat.id} was created')

            else:
                pro = Product.objects.create(name=f'{name}_product{i}',
                                             category_id=c)
                self.stdout.write(f'Product{pro.id} was created')


