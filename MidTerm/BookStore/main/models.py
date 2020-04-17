from django.db import models
import datetime
class BookJournalBase(models.Model):

    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=300)

    created_at = models.TimeField(default=datetime.time)



class Book(BookJournalBase):
    GENRE = [
        ('Criminal','Criminal'),
        ('Drama','Drama'),
        ('Mystery','Mystery'),
    ]
    num_pages = models.IntegerField
    genre = models.CharField(choices=GENRE,max_length=300)

class Journal(BookJournalBase):
    TYPE = [
        ('Bullet','Bullet'),
        ('Food','Food'),
        ('Travel','Travel'),
        ('Sport','Sport')
    ]
    type =models.CharField(choices=TYPE,max_length=300)
    publisher = models.CharField(max_length=200)


