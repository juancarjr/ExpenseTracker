from django.test import TestCase
import pytest
from trackerAPI import models
# Create your tests here.

@pytest.mark.django_db
def test_get_total_expense_method():
    for category in models.Category.objects.all():
        expense = models.Book.objects.get_total_expenses(category)
        assert expense == sum(b.distribution_expense for b in models.Book.objects.all().filter(category=category))