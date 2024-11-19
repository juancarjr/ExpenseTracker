from .models import Book, Category
import django_filters as filters
from django.db.models import Q
from django import forms
# class BookFilter(filters.FilterSet):
#     title = filters.CharFilter(lookup_expr='icontains')
#     authors = filters.CharFilter(lookup_expr='icontains')

class BookFilter(filters.FilterSet):
    search = filters.CharFilter(method='filter_by_all_fields', label='Search')

    start_date = filters.DateFilter(
        field_name='published_date',
        lookup_expr='gte',
        label='Date From',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    end_date = filters.DateFilter(
        field_name='published_date',
        lookup_expr='lte',
        label='Date To',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    category = filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Book
        fields = []

    def filter_by_all_fields(self, queryset, name, value):
        return queryset.filter(
            Q(authors__icontains=value) |
            Q(title__icontains=value) |
            Q(subtitle__icontains=value) |
            Q(category__name__icontains=value) |
            Q(publisher__name__icontains=value)
        )

