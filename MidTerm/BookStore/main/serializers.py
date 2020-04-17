from rest_framework import serializers
from .models import BookJournalBase,Book,Journal

class BookJournalBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookJournalBase
        fields = ('id','name','price','description','created_at')



class BookSerializer(BookJournalBaseSerializer):
    genre = serializers.CharField(read_only=True)
    num_pages = serializers.IntegerField(read_only=True)

    class Meta(BookJournalBaseSerializer.Meta):
        fields = BookJournalBaseSerializer.Meta.fields + ('genre','num_pages',)

    # def validate_(self,value):
    #     if value < 0:
    #         raise serializers.ValidationError('Num of pages must be positive')
    #     return value
    #

class JournalSerializer(BookJournalBaseSerializer):
    type = serializers.CharField(read_only=True)
    publisher = serializers.CharField(read_only=True)


    class Meta(BookJournalBaseSerializer.Meta):
        fields = BookJournalBaseSerializer.Meta.fields + ('id','type', 'publisher',)

    # def validate_type(self, value):
    #     if value  not in [
    #         ('1', 'Bullet'),
    #         ('2', 'Food'),
    #         ('3', 'Travel'),
    #         ('4', 'Sport'),
    #     ]:
    #         return serializers.ValidationError("type is incorrect")
    #     return value




