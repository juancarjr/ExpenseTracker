from . import models
from django.contrib import admin
from .models import Book
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Book


class BookResource(resources.ModelResource):

    class Meta:
        model = Book

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_classes = [BookResource]




