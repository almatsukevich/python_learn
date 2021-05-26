"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cities import views as cities_views
from dictionaries import views as dict_views

urlpatterns = [
#    path('', cities_views.cities_home),
    path('', dict_views.home, name = "manuals-home"),
    path('admin/', admin.site.urls),
    path('authors/', dict_views.author_list, name = "authors-list"),
    path('authors/<int:author_id>/', dict_views.author_detail, \
        name = "author"),
    path('bookseries/', dict_views.bookseries_list, name = "bookseries-list"),
    path('bookseries/<int:bookserie_id>/', dict_views.bookserie_detail, \
        name = "bookserie"),
    path('bookgenres/', dict_views.bookgenres_list, name = "bookgenres-list"),
    path('bookgenres/<int:bookgenre_id>/', dict_views.bookgenre_detail, \
        name = "bookgenre"),
    path('publishers/', dict_views.publisher_list, name = "publisher-list"),
    path('publishers/<int:publisher_id>/', dict_views.publisher_detail, \
        name = "publisher"),
    path('<str:code>/', cities_views.cities)
]
