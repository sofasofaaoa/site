from django.urls import path, include
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<slug:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<slug:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
] + [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]