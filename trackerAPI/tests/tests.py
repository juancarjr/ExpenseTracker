import pytest
from trackerAPI import models
from django.urls import reverse
from django.test import TestCase
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db
def test_get_total_expense_method():
    for category in models.Category.objects.all():
        expense = models.Book.objects.get_total_expenses(category)
        assert expense == sum(b.distribution_expense for b in models.Book.objects.all().filter(category=category))

# @pytest.mark.django_db
# def test_add_book(client):
