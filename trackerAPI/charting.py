import plotly.express as px
import pandas as pd
from .models import Book, Category

# def plot_book_expenses(qs):
#     print(qs)
#     total_expenses = {}
#     for category in Category.objects.all():
#         total_expenses[category.name] = Book.objects.get_expenses(category)

#     df = pd.DataFrame(total_expenses.items(), columns=['Category', 'Total Expenses'])
#     df = df.sort_values(by='Total Expenses', ascending=True)

#     fig = px.bar(
#         df,
#         x='Category',
#         y='Total Expenses',
#         title='Total Expenses by Category'
#     )
#     # fig.show()
#     return fig.to_html()

def plot_book_expenses(qs):
    data = []
    for book in qs:
        category_name = book.category.name
        expense = book.distribution_expense
        data.append({'Category': category_name, 'Total Expenses': expense})

    df = pd.DataFrame(data)
    df = df.groupby('Category').sum().reset_index()
    df = df.sort_values(by='Total Expenses', ascending=True)

    fig = px.bar(
        df,
        x='Category',
        y='Total Expenses',
        title='Total Expenses by Category'
    )
    return fig.to_html()


def plot_book_expenses_pie(qs):
    data = []
    for book in qs:
        category_name = book.category.name
        expense = book.distribution_expense
        data.append({'Category': category_name, 'Total Expenses': expense})
        
    df = pd.DataFrame(data)
    df = df.groupby('Category').sum().reset_index()

    fig = px.pie(
        df,
        names='Category',
        values='Total Expenses',
        title='Total Expenses by Category'
    )
    return fig.to_html()