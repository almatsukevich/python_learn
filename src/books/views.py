from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . import models, forms
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.

class BookDetailView(DetailView):
    model = models.Book

class BookListView(ListView):
    model = models.Book
    paginate_by = 12

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = models.Book
    form_class = forms.CreateBookForm
    success_url = reverse_lazy('books:book-list')
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    permission_required = ('books.add_book')

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.Book
    form_class = forms.CreateBookForm
    success_url = reverse_lazy('books:book-list')
    login_url = '/accounts/login/'
    permission_required = ('books.change_book')

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Book
    success_url = reverse_lazy('books:book-list')
    login_url = '/accounts/login/'
    permission_required = ('books.delete_book')


class Home(TemplateView):
    template_name = 'home.html'