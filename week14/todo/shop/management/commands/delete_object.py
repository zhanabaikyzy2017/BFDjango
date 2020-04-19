from django.core.management.base import BaseCommand
from shop.models import Product, Category

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('ids', nargs='+', help = 'Ids of objects to delete')
        parser.add_argument('-ifcat', '--ifcategory', action='store_true', help = 'Flag to delete Category objects instead Product')


    def handle(self, *args, **kwargs):

        ifcat = kwargs.get('ifcategory')


        if not ifcat:
            for id in kwargs.get('ids'):
                try:
                    cat = Category.objects.get(id = id)
                    cat.delete()
                    self.stdout.write(self.style.SUCCESS(f'Category id: {id} deleted successfully'))
                except Category.DoesNotExist as e:
                    self.stdout.write(self.style.ERROR(f'Category id: {id} does not exist!'))
        else:
            for id in kwargs.get('ids'):
                try:
                    pro = Product.objects.get(id = id)
                    pro.delete()
                    self.stdout.write(self.style.SUCCESS(f'Product id: {id} deleted successfully'))
                except Product.DoesNotExist as e:
                    self.stdout.write(self.style.ERROR(f'Product id: {id} does not exist!'))

