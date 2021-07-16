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

    def get_queryset(self):
        qs=super().get_queryset()
        filter = self.request.GET.get('filter')
        author_pk = self.request.GET.get('author_pk')
        genre_pk = self.request.GET.get('genre_pk')
        serie_pk = self.request.GET.get('serie_pk')
        publusher_pk = self.request.GET.get('publusher_pk')
        if filter == 'name':
            return qs.order_by('name')
        if filter == 'rating':
            return qs.order_by('-rating')
        if author_pk:
            return qs.filter(author__pk=int(author_pk))
        if genre_pk:
            return qs.filter(genre__pk=int(genre_pk))
        if serie_pk:
            return qs.filter(serie__pk=int(serie_pk))
        if publusher_pk:
            return qs.filter(publusher__pk=int(publusher_pk))
        return qs

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