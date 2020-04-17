from rest_framework import serializers
from .models import Product, Category
from auth_.serializer import MyUserSerializer


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    type = serializers.CharField(max_length=200)
    created_by = MyUserSerializer(read_only=True,)

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

    def count_validator(value):
        if value<0:
            raise serializers.ValidationError('product should be more than 1.')


    # category = CategorySerializer(read_only=True)
    price = serializers.FloatField(required=True)
    count = serializers.IntegerField(required=True, validators = [count_validator])
    status = serializers.IntegerField(required=True)

    # из за default трабл решен!!!

    class Meta:
        model = Product
        fields = '__all__'


    def validate_price(self,value):
        if value<0:
            raise serializers.ValidationError('invalid price haha')
        return value

