from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.BookItemsView.as_view(), name='books'),
    path('books/<int:pk>', views.SingleBookItemView.as_view(), name='singlebook'),
]