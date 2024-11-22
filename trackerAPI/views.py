from django.shortcuts import render
from .models import Book, Category
from .filters import BookFilter
from .forms import BookForm
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_htmx.http import retarget
#TODO: WRITE TESTS

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
        total_expenses[category] = Book.objects.get_expenses(category)

    query_expense = Book.objects.get_total_expenses()
    context = {'books': books,
               'totals': total_expenses,
               'query_expense': query_expense}

    

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
