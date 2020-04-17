from django.shortcuts import render
from .models import Book,Journal
from .serializers import BookSerializer,JournalSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class BookListViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []


class BookList(
               mixins.ListModelMixin,
                mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # lookup_field ='book_id'

    def get(self, request, *args, **kwargs):
        # self.top_ten()
        return self.list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BookDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'book_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class JournalViewSet(viewsets.ModelViewSet):

    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


