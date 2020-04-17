from .models import Product,Category
from .serializers import ProductSerilizer,CategorySerializer
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import action
from rest_framework.response import Response



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
        return Category.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)


    @action(methods=['GET',], detail=True)
    def products(self,request,pk):
        print("ok")
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

    queryset = Product.objects.all()
    serializer_class = ProductSerilizer
    permission_classes = (IsAuthenticated,)



