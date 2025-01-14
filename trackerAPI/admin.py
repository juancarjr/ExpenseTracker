from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Book, Category, Publisher, UserProfile, Favorite


class BookResource(resources.ModelResource):

    class Meta:
        model = Book

class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category

class PublisherResource(resources.ModelResource):

    class Meta:
        model = Publisher

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_classes = [BookResource]
    search_fields = ['title', 'authors', 'published_date', 'subtitle' ]
    list_display = ['title', 'publisher', 'published_date', 'distribution_expense']
    list_filter = ['category', 'publisher']
    ordering = ['title', 'published_date']
    date_hierarchy = 'published_date'
    empty_value_display = ' NONE'

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_classes = [CategoryResource]

@admin.register(Publisher)
class PublisherAdmin(ImportExportModelAdmin):
    resource_classes = [PublisherResource]

admin.site.register(UserProfile)
admin.site.register(Favorite)