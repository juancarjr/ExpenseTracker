from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


def index(request):
    return render(request, 'index.html', {})

def books_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'transactions-list.html', context)

# def about(request):
#     return render(request, 'about.html')

# def menu(request):
#     menu_data = Menu.objects.all()
#     main_data = {"menu": menu_data}
#     return render(request, 'menu.html', {"menu": main_data})

class SingleBookItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookItemsView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]