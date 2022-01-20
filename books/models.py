from django.db import models


class Speakers(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)


class Authors(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)


class Category(models.Model):
    name = models.CharField(max_length=64)


class Book(models.Model):
    ELECTRONIC_BOOK = 1
    VOCAL_BOOK = 2

    BOOK_STATUS = (
        (ELECTRONIC_BOOK, 'electronic book'),
        (VOCAL_BOOK, 'vocal book')
    )

    price = models.IntegerField(default=0)
    author = models.ForeignKey(Authors, on_delete=models.SET_NULL, related_name='books', null=True)
    name = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='books', null=True)
    book_type = models.PositiveIntegerField(choices=BOOK_STATUS)


class ElectronicBook(models.Model):
    shobak = models.CharField(max_length=25)
    page_count = models.IntegerField(default=0)
    printed_book = models.IntegerField(default=0)
    published_year = models.DateField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='details_electronic_book')


class VocalBook(models.Model):
    copy_status = models.BooleanField(default=True)
    speaker = models.ForeignKey(Speakers, on_delete=models.SET_NULL, related_name='spoke_book', null=True)
