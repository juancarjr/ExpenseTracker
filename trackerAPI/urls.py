from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books_list, name='books_list'),
    path('add/', views.add_book, name='add_book'),
    path('favorites/', views.favorites, name='favorites'),
    path('delete/<int:pk>', views.favorites_delete, name='favorites-delete'),
    path('add/<int:pk>', views.favorites_add, name='favorites-add'),
    path('get-books', views.get_books, name='get-books'),
]