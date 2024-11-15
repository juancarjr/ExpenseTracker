from django.db import models

class BookQueryset(models.QuerySet):
    def get_total_expenses(self, category):
        return self.filter(models.Q(category__name__iexact=category)).aggregate(
            total=models.Sum('distribution_expense')
            )['total'] or 0
     