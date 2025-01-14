from django.db import models

#TODO: WRITE TESTS FOR get_total_expenses

class BookQueryset(models.QuerySet):
    def get_expenses(self, category):
        return self.filter(models.Q(category__name__iexact=category)).aggregate(
            total=models.Sum('distribution_expense')
            )['total'] or 0
    
    def get_total_expenses(self):
        return self.aggregate(total=models.Sum('distribution_expense'))['total']
