from django.contrib import admin
from .models import Book,ImportantPoints,WishList
# Register your models here.
admin.site.register(Book)
admin.site.register(ImportantPoints)
admin.site.register(WishList)
