from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Book, Category, Favorite
from .filters import BookFilter, FavoriteFilter
from .forms import BookForm
from .charting import plot_book_expenses, plot_book_expenses_pie
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_htmx.http import retarget
from datetime import datetime
from django.core.paginator import Paginator

#TODO: WRITE TESTS, FAVORITES LIST

def index(request):
    return render(request, 'index.html', {})

def books_list(request):
    page_num = request.GET.get('page', 1)
    books = BookFilter(
        request.GET,
        queryset = Book.objects.all().select_related('category', 'publisher')
    )

    total_expenses = {}
    for category in Category.objects.all():
        total_expenses[category] = Book.objects.get_expenses(category)

    PAGE_SIZE = 30
    query_expense = Book.objects.get_total_expenses()
    paginator = Paginator(books.qs, PAGE_SIZE)
    page_obj = paginator.get_page(page_num)

    context = {'books': books,
               'totals': total_expenses,
               'query_expense': query_expense,
               'page_obj': page_obj}

    if request.htmx:
        return render(request, 'partials/books-container.html', context)

    return render(request, 'books-list.html', context)

@permission_classes([IsAuthenticated])
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'message': 'Book added successfully!'}
            return render(request, 'partials/book-success.html', context)
        else: 
            context = {'form': form}
            for k,v in form.errors.items():
                print(k, v)
            response =  render(request, 'partials/add-book.html', context)
            return retarget(response, '#book-block')

    
    context = {'form': BookForm}
    return render(request, 'partials/add-book.html', context)

@permission_classes([IsAuthenticated])
def favorites(request):
    favorites = FavoriteFilter(
        request.GET,
        queryset = Favorite.objects.all().filter(user=request.user).select_related('user', 'book')
    )
    context = {'favorites': favorites}
    if request.htmx:
        return render(request, 'partials/favorite-container.html', context)
    return render(request, 'favorite-list.html', context)

@permission_classes([IsAuthenticated])
def favorites_delete(request, pk):
    Favorite.objects.filter(id=pk).delete()
    favorites = FavoriteFilter(
        request.GET,
        queryset = Favorite.objects.all().filter(user=request.user).select_related('user', 'book')
    )
    context = {'favorites': favorites}
    if request.htmx:
        return render(request, 'partials/favorite-container.html', context)
    
@permission_classes([IsAuthenticated])
def favorites_add(request, pk):
    Favorite.objects.create(user=request.user, book=Book.objects.get(id=pk), date_added=datetime.now())
    books = BookFilter(
        request.GET,
        queryset = Book.objects.all().select_related('category', 'publisher')
    )
    total_expenses = {}
    for category in Category.objects.all():
        total_expenses[category] = Book.objects.get_expenses(category)
    query_expense = Book.objects.get_total_expenses()
    context = {'books': books,
               'totals': total_expenses,
               'query_expense': query_expense}
    if request.htmx:
        return render(request, 'partials/books-container.html', context)
    
def get_books(request):
    page = request.GET.get('page', 1)
    books = BookFilter(
        request.GET,
        queryset = Book.objects.all().select_related('category', 'publisher')
    )
    PAGE_SIZE = 30
    paginator = Paginator(books.qs, PAGE_SIZE)
    context = {'page_obj': paginator.get_page(page)}
    return render(request, 'partials/books-container.html#infinite_list', context)

def get_charts(request):
    books = BookFilter(
        request.GET,
        queryset = Book.objects.all().select_related('category', 'publisher')
    )

    total_expenses = {}
    for category in Category.objects.all():
        total_expenses[category] = Book.objects.get_expenses(category)

    book_expenses_bar = plot_book_expenses(books.qs)
    book_expenses_pie = plot_book_expenses_pie(books.qs)

    context = {'books': books,
               'totals': total_expenses,
               'query_expense': Book.objects.get_total_expenses(),
               'book_expenses_bar': book_expenses_bar,
               'book_expenses_pie': book_expenses_pie}

    if request.htmx:
        return render(request, 'partials/charts-container.html', context)
    return render(request, 'charts.html', context)