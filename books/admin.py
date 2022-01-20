from django.contrib import admin
from books.models import Book, VocalBook, ElectronicBook, Speakers, Authors, Category

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Authors)
admin.site.register(Speakers)
admin.site.register(ElectronicBook)
admin.site.register(VocalBook)
