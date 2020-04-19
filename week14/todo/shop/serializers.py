from rest_framework import serializers
from .models import Product, Category
from auth_.serializer import MyUserSerializer


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)
    type = serializers.CharField(max_length=200)
    created_by = MyUserSerializer(read_only=True,)
    products_count = serializers.IntegerField(default=0)

    def create(self, validated_data):
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance,validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance


class ProductSerilizer(serializers.ModelSerializer):
    category = CategorySerializer
    price = serializers.FloatField(required=True)
    count = serializers.IntegerField(required=True)
    status = serializers.IntegerField(required=True)
    # picture = serializers.ImageField(required=True)
    category_type = serializers.CharField(source='category.type')

    class Meta:
        model = Product
        fields = ('id','name','price','count','status','category','picture','category_type')
