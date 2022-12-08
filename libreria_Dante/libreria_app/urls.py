from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    # URL Iniciales
    path('',views.inicio,name='inicio'),
    path('index',views.index,name='index'),
    # URL BOOKS
    path('createBook',views.createBook,name="createBook"),
    path('readBooks',views.readBooks,name='readBooks'),
    path('updateBook',views.updateBook,name='updateBook'),
    path('deleteBook/<int:id>',views.deleteBook,name='deleteBook'),
    path('updateBooks/<int:id>',views.updateBook,name='updateBook'),
     
    #URL WISH LIST
    path('addBookWishList',views.addBookWishList,name="addBookWishList"),
    path('readBooksWishList',views.readBooksWishList,name='readBooksWishList'),
    path('updateBookWishList',views.updateBookWishList,name='updateBookWishList'),
    path('deleteBookWishList/<int:id>',views.deleteBookWishList,name='deleteBookWishList'),
    path('updateBookWishList/<int:id>',views.updateBookWishList,name='updateBookWishList'),
   
    #URL Important Points
    # path('readImportantPoints',views.readImportantPoints,name="readImportantPoints"),
    # path('createImportantPoint',views.createImportantPoint,name='createImportantPoint'),
    # path('updateImportantPoints',views.updateImportantPoints,name='updateImportantPoints'),
    path('createImportantPoint/<int:id>',views.createImportantPoint,name='createImportantPoint'),
    path('updateImportantPoints/<int:id>',views.updateImportantPoints,name='updateImportantPoints'),
    path('deleteImportantPoints/<int:id>',views.deleteImportantPoints,name='deleteImportantPoints'),
    path('readImportantPoints/<int:id>',views.readImportantPoints,name="readImportantPoints"),
    
    # URL ABOUT
    path('about',views.about,name='about'),
    path('report',views.report,name='report'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
