from django.urls import path
from books import views as book_views

app_name = 'books'

urlpatterns = [
    path('', book_views.BookListView.as_view(), name = "book-list"),
    path('<int:pk>/', book_views.BookDetailView.as_view(), \
        name = "book"),
    path('book-create/', book_views.BookCreateView.as_view(), \
        name = "book-create"),
    path('book-update/<int:pk>/', book_views.BookUpdateView.as_view(), \
        name = "book-update"),
    path('book-delete/<int:pk>/', book_views.BookDeleteView.as_view(), \
        name = "book-delete")
]