from django.urls import path
from dictionaries import views as dict_views

app_name = 'manuals'

urlpatterns = [
    path('', dict_views.ManualsHome.as_view(), name = "manuals-home"),
    path('authors/', dict_views.AuthorListView.as_view(), name = "authors-list"),
    path('authors/<int:pk>/', dict_views.AuthorDetailView.as_view(), \
        name = "author"),
    path('author-create/', dict_views.AuthorCreateView.as_view(), \
        name = "author-create"),
    path('author-update/<int:pk>/', dict_views.AuthorUpdateView.as_view(), \
        name = "author-update"),
    path('author-delete/<int:pk>/', dict_views.AuthorDeleteView.as_view(), \
        name = "author-delete"),

    path('bookseries/', dict_views.BookSeriesListView.as_view(), name = "bookseries-list"),
    path('bookseries/<int:pk>/', dict_views.BookSeriesDetailView.as_view(), \
        name = "bookseries"),
    path('bookseries-create/', dict_views.BookSeriesCreateView.as_view(), \
        name = "bookseries-create"),
    path('bookseries-update/<int:pk>/', dict_views.BookSeriesUpdateView.as_view(), \
        name = "bookseries-update"),
    path('bookseries-delete/<int:pk>/', dict_views.BookSeriesDeleteView.as_view(), \
        name = "bookseries-delete"),

    path('bookgenres/', dict_views.BookGenreListView.as_view(), name = "bookgenres-list"),
    path('bookgenre/<int:pk>/', dict_views.BookGenreDetailView.as_view(), \
        name = "bookgenre"),
    path('bookgenre-create/', dict_views.BookGenreCreateView.as_view(), \
        name = "bookgenre-create"),
    path('bookgenre-update/<int:pk>/', dict_views.BookGenreUpdateView.as_view(), \
        name = "bookgenre-update"),
    path('bookgenre-delete/<int:pk>/', dict_views.BookGenreDeleteView.as_view(), \
        name = "bookgenre-delete"),

    path('publishers/', dict_views.PublusherListView.as_view(), name = "publishers-list"),
    path('publishers/<int:pk>/', dict_views.PublusherDetailView.as_view(), \
        name = "publisher"),
    path('publisher-create/', dict_views.PublusherCreateView.as_view(), \
        name = "publisher-create"),
    path('publisher-update/<int:pk>/', dict_views.PublusherUpdateView.as_view(), \
        name = "publisher-update"),
    path('publisher-delete/<int:pk>/', dict_views.PublusherDeleteView.as_view(), \
        name = "publisher-delete"),

    # path('bookseries/', dict_views.bookseries_list, name = "bookseries-list"),
    # path('bookseries/<int:bookserie_id>/', dict_views.bookserie_detail, \
    #     name = "bookserie"),
    # path('bookgenres/', dict_views.bookgenres_list, name = "bookgenres-list"),
    # path('bookgenres/<int:bookgenre_id>/', dict_views.bookgenre_detail, \
    #     name = "bookgenre"),
    # path('publishers/', dict_views.publisher_list, name = "publisher-list"),
    # path('publishers/<int:publisher_id>/', dict_views.publisher_detail, \
    #     name = "publisher")
]