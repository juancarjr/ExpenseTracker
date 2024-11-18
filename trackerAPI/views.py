from django.shortcuts import render
from rest_framework import generics
from .models import Book, Category
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import BookFilter

def index(request):
    return render(request, 'index.html', {})

def books_list(request):
    # books = Book.objects.all()
    books = BookFilter(
        request.GET,
        queryset = Book.objects.all().select_related('category', 'publisher')
    )
    total_expenses = {}
    for category in Category.objects.all():
        total_expenses[category] = Book.objects.get_total_expenses(category)

    context = {'books': books,
               'totals': total_expenses}

    

    if request.htmx:
        return render(request, 'partials/books-container.html', context)

    return render(request, 'books-list.html', context)

class SingleBookItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookItemsView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]