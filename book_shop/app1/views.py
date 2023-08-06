from django.shortcuts import render,redirect
from .forms import BookStoreForms
from app1.models import BookStoreModel
from django.utils import timezone

def home(request):
    return render(request,'base.html')

def storebook(request):
    if request.method == 'POST':
        book=BookStoreForms(request.POST)
        if book.is_valid():
            print(book.cleaned_data)
            book.save()
            return redirect('showbook')
    else:
        book=BookStoreForms()
        
    return render(request,'store_book.html',{'form':book})

def showbooks(request):
    book=BookStoreModel.objects.all()
    print(book)
    return render(request,'show_book.html',{'data': book})

def edit_book(request, id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForms(instance = book)
    if request.method == 'POST':
        form = BookStoreForms(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect('showbook')
    return render(request, 'store_book.html', {'form':form})

    