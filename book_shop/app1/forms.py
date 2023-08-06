from django import forms
from . models import BookStoreModel


class BookStoreForms(forms.ModelForm):
    class Meta:
        model=BookStoreModel
        fields=['id','book_name','catagory','about']
    