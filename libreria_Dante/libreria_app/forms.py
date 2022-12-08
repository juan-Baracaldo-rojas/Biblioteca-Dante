from pyexpat import model
from django import forms
from .models import Book,WishList,ImportantPoints

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"
class BookWishListForm(forms.ModelForm):
    class Meta:
        model=WishList
        fields="__all__"
class ImportantPointsForm(forms.ModelForm):
    class Meta:
        model=ImportantPoints
        fields="__all__"