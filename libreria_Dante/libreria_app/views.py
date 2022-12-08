
from ctypes.wintypes import POINT
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Book, ImportantPoints,WishList
from .forms import BookForm,BookWishListForm,ImportantPointsForm
# Create your views here.
# vistas Iniciales
def inicio(request):
    return HttpResponse("<h1> Estoy Vivo !!! <h1>")

def index(request):
    return render(request,'Pages/index.html')

# Vistas Book
def createBook(request):
    formularioBook=BookForm(request.POST or None,request.FILES or None)
    print('valores formulario {}'.format(formularioBook.data))
    if formularioBook.is_valid():
        formularioBook.save()
        return redirect('readBooks')
    return render(request,"PagesBooks/createBook.html",{'formularioBook':formularioBook})

def readBooks(request):
    books=Book.objects.all()
    return render(request,"PagesBooks/readBooks.html",{'books':books})
 
def updateBook(request,id):
    book=Book.objects.get(id=id)
    formUpdateBook=BookForm(request.POST or None,request.FILES or None, instance=book)
    if formUpdateBook.is_valid() and request.POST:
        formUpdateBook.save()
        return redirect('readBooks')
    return render(request,"PagesBooks/updateBook.html",{'formularioBook':formUpdateBook})

def deleteBook(request,id):
    bookd=Book.objects.get(id=id)
    bookd.delete()
    return redirect('readBooks')

# Vistas Lista de Deseos
def addBookWishList(request):
    formularioBookWishList=BookWishListForm(request.POST or None,request.FILES or None)
    if formularioBookWishList.is_valid():
        formularioBookWishList.save()
        return redirect('readBooksWishList')
    return render(request,"PagesWishList/addBookWishList.html",{'formularioBookWishList':formularioBookWishList})

def readBooksWishList(request):
    booksWishList=WishList.objects.all()
    return render(request,"PagesWishList/readBooksWishList.html",{'booksWishList':booksWishList})

def updateBookWishList(request,id):
    booksWishList=WishList.objects.get(id=id)
    formUpdateBookWishList=BookWishListForm(request.POST or None,request.FILES or None,instance=booksWishList)
    if formUpdateBookWishList.is_valid():
        formUpdateBookWishList.save()
        return redirect('readBooksWishList')
    return render(request,"PagesWishList/updateBookWishList.html",{'formularioBookWishList':formUpdateBookWishList})

def deleteBookWishList(request,id):
    bookWishList=WishList.objects.get(id=id)
    bookWishList.delete()
    return redirect('readBooksWishList')
#TODO vincular direcciones id de metodos create y update
#TODO generar vista de reportes
#TODO dead line 04/05/2021
# Vistas Apuntes
def createImportantPoint(request,id):
    #lista de libros
    book=Book.objects.get(id=id)
    books=Book.objects.all()
    formularioImportantPoints=ImportantPointsForm(request.POST or None,request.FILES or None)
    if formularioImportantPoints.is_valid():
        formularioImportantPoints.save()
        return redirect('readImportantPoints',{'id':id})
    return render(request,"PagesImportanPoints/createImportantPoint.html",{'formularioImportantPoints':formularioImportantPoints,'bookSelect':book,'books':books,'idLibro':id})

def readImportantPoints(request,id):
    book=Book.objects.get(id=id)
    importantPoints=ImportantPoints.objects.all()
    return render(request,"PagesImportanPoints/readImportantPoints.html",{'importantPoints':importantPoints,'bookSelect':book})

def updateImportantPoints(request,id):
    importanPoint=ImportantPoints.objects.get(id=id)
    formUpdateImportantPoint=ImportantPointsForm(request.POST or None,request.FILES or None,instance=importanPoint)
    if formUpdateImportantPoint.is_valid():
        formUpdateImportantPoint.save()
        return redirect('readImportantPoints',{'idImportantPoint':id})
    return render(request,"PagesImportanPoints/updateImportantPoints.html",{'formularioImportantPoints':formUpdateImportantPoint,'nt':importanPoint})

def deleteImportantPoints(request,id):
    importantPoint=ImportantPoints.objects.get(id=id)
    importantPoint.delete()
    return redirect('readImportantPoints',{'id':id})

# Vista About us
def about(request):
    return render(request,"Pages/about.html")

# Vista Report
def report(request):
    return render(request,"Pages/report.html")
