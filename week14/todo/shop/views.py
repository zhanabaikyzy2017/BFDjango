from .models import Product,Category
from .serializers import ProductSerilizer,CategorySerializer
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import action
from rest_framework.response import Response
import logging
from django.db.models import Avg, Min, Max, Sum, Count, F
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

logger2 = logging.getLogger(__name__)
logger = logging.getLogger('shopp')




class CategoryListViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    # queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Category.objects.for_user(user=self.request.user).annotate(products_count=Count('products'))

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)
        logger2.info(f'new Category created by: {serializer.instance.id}')


    @action(methods=['GET',], detail=True)
    def products(self,request,pk):
        try:
            products = Product.objects.filter(category = Category.objects.get(id=self.kwargs.get('pk')))
        except ObjectDoesNotExist:
            raise Http404
        serializer = ProductSerilizer(products, many=True)
        return Response(serializer.data)


class ProductListViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):


    serializer_class = ProductSerilizer
    # permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    # queryset = Product.objects.all()
    def get_queryset(self):
        if self.action == 'list':
            return Product.objects.select_related('category')
        return Product.status_check.all()


    def perform_create(self, serializer):
        serializer.save()
        # logger.info(f'New Product created, NAME: {serializer.instance.name}')
        # logger.warning(f'New Product created, NAME: {serializer.instance.name}')
        # logger.debug(f'New Product created, NAME: {serializer.instance.id}')
        logger2.info(f'new Product created by: {self.request.user}')

    @action(methods=['GET'], detail=False)
    def price_report(self, request):
        data = [
            Product.objects.aggregate(Avg('price')),
            Category.objects.values('name').annotate(Count('products'))
        ]

        return Response(data)
    @action(methods=['GET'], detail=True)
    def price_update(selfself, request, pk):
        Product.objects.update(price=F('price')+pk)
        return Response("ok")




