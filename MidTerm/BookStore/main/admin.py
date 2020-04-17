from django.contrib import admin
from .models import BookJournalBase,Book,Journal


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','description','genre','num_pages')

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','description','type','publisher')

