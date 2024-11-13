from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    published_date = models.DateField(null=True)
    category = models.CharField(max_length=200)
    distribution_expense = models.DecimalField(null=False, max_digits=5, decimal_places=2)

    def __str__(self): 
        return self.title


