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
from django.urls import path, include
from django.urls.conf import include

from cities import views as cities_views
from dictionaries import views as dict_views

urlpatterns = [
    path('', dict_views.Home.as_view(), name = 'home'),
    path('manuals/', include('dictionaries.urls', namespace = 'manuals')),
    path('admin/', admin.site.urls),
#    path('authors/', dict_views.author_list, name = "authors-list"),
    # path('authors/', dict_views.AuthorListView.as_view(), name = "authors-list"),
    # path('authors/<int:author_id>/', dict_views.author_detail, \
    #     name = "author"),
    # path('authors/<int:pk>/', dict_views.AuthorDetailView.as_view(), \
    #     name = "author"),
    # path('author-create/', dict_views.AuthorCreateView.as_view(), \
    #     name = "author-create"),
    # path('author-update/<int:pk>/', dict_views.AuthorUpdateView.as_view(), \
    #     name = "author-update"),
    # path('author-delete/<int:pk>/', dict_views.AuthorDeleteView.as_view(), \
    #     name = "author-delete"),

 #   path('<str:code>/', cities_views.cities)
]
