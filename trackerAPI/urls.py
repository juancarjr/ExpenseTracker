from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books_list, name='books_list'),
    path('add/', views.add_book, name='add_book'),
]