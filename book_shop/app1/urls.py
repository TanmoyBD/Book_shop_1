from django.urls import path
from app1.views import home

from django.urls import path
from app1.views import home, storebook, showbooks,edit_book

urlpatterns = [
    path('', home),
    path('storebook/', storebook,name = 'store_book'),
    path('showbooks/', showbooks,name ='showbook'),
    path('edit_book/<int:id>', edit_book,name = 'edit_book'),
]
