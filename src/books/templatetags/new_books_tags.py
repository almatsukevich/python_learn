from django import template
from .. import models
register = template.Library()

@register.inclusion_tag('books/tags/show_new_books.html')
def show_new_books():
    new_books = models.Book.objects.order_by('-created')[:8]
    return {'new_books': new_books }

@register.inclusion_tag('books/tags/show_popular_books.html')
def show_popular_books():
    popular_books = models.Book.objects.order_by('-num_orders')[:8]
    return {'popular_books': popular_books }

@register.inclusion_tag('books/tags/show_random_books.html')
def show_random_books():
    random_books = models.Book.objects.order_by('?')[:8]
    return {'random_books': random_books }