from django.shortcuts import render

from . import models

# Create your views here.

# Create home view
def home(request):
    return render(request, template_name="manuals_home.html", context = {})


def author_detail(request, author_id):
    author = models.Author.objects.get(pk=author_id)
    ctx = {
            'author': author
        }
    return render(request, template_name="author_detail.html", context = ctx)

def author_list(request):
    author_list = models.Author.objects.all()
    ctx = {
            'author_list': author_list
        }
    return render(request, template_name="author_list.html", context = ctx)



def bookserie_detail(request, bookserie_id):
    bookserie = models.BookSeries.objects.get(pk=bookserie_id)
    ctx = {
            'bookserie': bookserie
        }
    return render(request, template_name="bookserie_detail.html", context = ctx)

def bookseries_list(request):
    bookseries_list = models.BookSeries.objects.all()
    ctx = {
            'bookseries_list': bookseries_list
        }
    return render(request, template_name="bookseries_list.html", context = ctx)



def bookgenre_detail(request, bookgenre_id):
    bookgenre = models.BookGenre.objects.get(pk=bookgenre_id)
    ctx = {
            'bookgenre': bookgenre
        }
    return render(request, template_name="bookgenre_detail.html", context = ctx)

def bookgenres_list(request):
    bookgenres_list = models.BookGenre.objects.all()
    ctx = {
            'bookgenres_list': bookgenres_list
        }
    return render(request, template_name="bookgenres_list.html", context = ctx)



def publisher_detail(request, publisher_id):
    publisher = models.Publusher.objects.get(pk=publisher_id)
    ctx = {
            'publisher': publisher
        }
    return render(request, template_name="publisher_detail.html", context = ctx)

def publisher_list(request):
    publisher_list = models.Publusher.objects.all()
    ctx = {
            'publisher_list': publisher_list
        }
    return render(request, template_name="publisher_list.html", context = ctx)