from django.db import models
from .managers import BookQueryset

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

class Publisher(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
    
class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    subtitle = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    published_date = models.DateField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    distribution_expense = models.DecimalField(null=False, max_digits=5, decimal_places=2)

    objects = BookQueryset.as_manager()

    
    def __str__(self): 
        return self.title

    class Meta:
        ordering = ['title']


    
