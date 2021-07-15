from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . import models, forms
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.

# Create home view
# def home(request):
#     return render(request, template_name="manuals_home.html", context = {})

class ManualsHome(TemplateView):
    template_name = 'dictionaries/manuals_home.html'

# def author_detail(request, author_id):
#     author = models.Author.objects.get(pk=author_id)
#     ctx = {
#             'author': author
#         }
#     return render(request, template_name="author_detail.html", context = ctx)
class AuthorDetailView(DetailView):
    model = models.Author


# def author_list(request):
#     author_list = models.Author.objects.all()
#     ctx = {
#             'author_list': author_list
#         }
#     return render(request, template_name="author_list.html", context = ctx)
class AuthorListView(ListView):
    model = models.Author
    paginate_by = 20
class AuthorCreateView(PermissionRequiredMixin, CreateView):
    model = models.Author
    form_class = forms.CreateAuthorForm
    success_url = reverse_lazy('manuals:authors-list')
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    permission_required = ('dictionaries.add_author')

class AuthorUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.Author
    form_class = forms.CreateAuthorForm
    success_url = reverse_lazy('manuals:authors-list')
    login_url = '/accounts/login/'
    permission_required = ('dictionaries.change_author')

class AuthorDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Author
    success_url = reverse_lazy('manuals:authors-list')
    login_url = '/accounts/login/'
    permission_required = ('dictionaries.delete_author')


# def bookserie_detail(request, bookserie_id):
#     bookserie = models.BookSeries.objects.get(pk=bookserie_id)
#     ctx = {
#             'bookserie': bookserie
#         }
#     return render(request, template_name="bookserie_detail.html", context = ctx)

# def bookseries_list(request):
#     bookseries_list = models.BookSeries.objects.all()
#     ctx = {
#             'bookseries_list': bookseries_list
#         }
#     return render(request, template_name="bookseries_list.html", context = ctx)

class BookSeriesDetailView(DetailView):
    model = models.BookSeries
class BookSeriesListView(ListView):
    model = models.BookSeries
    paginate_by = 20
class BookSeriesCreateView(PermissionRequiredMixin, CreateView):
    model = models.BookSeries
    form_class = forms.CreateBookSeriesForm
    success_url = reverse_lazy('manuals:bookseries-list')
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    permission_required = ('dictionaries.add_bookseries')
class BookSeriesUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.BookSeries
    form_class = forms.CreateBookSeriesForm
    success_url = reverse_lazy('manuals:bookseries-list')
    login_url = '/accounts/login/'
    permission_required = ('dictionaries.change_bookseries')
class BookSeriesDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.BookSeries
    success_url = reverse_lazy('manuals:bookseries-list')
    login_url = '/accounts/login/'
    permission_required = ('dictionaries.delete_bookseries')


# def bookgenre_detail(request, bookgenre_id):
#     bookgenre = models.BookGenre.objects.get(pk=bookgenre_id)
#     ctx = {
#             'bookgenre': bookgenre
#         }
#     return render(request, template_name="bookgenre_detail.html", context = ctx)

# def bookgenres_list(request):
#     bookgenres_list = models.BookGenre.objects.all()
#     ctx = {
#             'bookgenres_list': bookgenres_list
#         }
#     return render(request, template_name="bookgenres_list.html", context = ctx)

class BookGenreDetailView(DetailView):
    model = models.BookGenre
class BookGenreListView(ListView):
    model = models.BookGenre
    paginate_by = 20
class BookGenreCreateView(PermissionRequiredMixin, CreateView):
    model = models.BookGenre
    form_class = forms.CreateBookGenreForm
    success_url = reverse_lazy('manuals:bookgenres-list')
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    permission_required = ('dictionaries.add_bookgenre')
class BookGenreUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.BookGenre
    form_class = forms.CreateBookGenreForm
    success_url = reverse_lazy('manuals:bookgenres-list')
    login_url = '/accounts/login/'
    permission_required = ('dictionaries.change_bookgenre')
class BookGenreDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.BookGenre
    success_url = reverse_lazy('manuals:bookgenres-list')
    login_url = '/accounts/login/'
    permission_required = ('dictionaries.delete_bookgenre')



# def publisher_detail(request, publisher_id):
#     publisher = models.Publusher.objects.get(pk=publisher_id)
#     ctx = {
#             'publisher': publisher
#         }
#     return render(request, template_name="publisher_detail.html", context = ctx)

# def publisher_list(request):
#     publisher_list = models.Publusher.objects.all()
#     ctx = {
#             'publisher_list': publisher_list
#         }
#     return render(request, template_name="publisher_list.html", context = ctx)

class PublusherDetailView(DetailView):
    model = models.Publusher
class PublusherListView(ListView):
    model = models.Publusher
    paginate_by = 20
class PublusherCreateView(PermissionRequiredMixin, CreateView):
    model = models.Publusher
    form_class = forms.CreatePublusherForm
    success_url = reverse_lazy('manuals:publishers-list')
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    permission_required = ('dictionaries.add_publusher')

class PublusherUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.Publusher
    form_class = forms.CreatePublusherForm
    success_url = reverse_lazy('manuals:publishers-list')
    login_url = '/accounts/login/'
    permission_required = ('dictionaries.change_publusher')

class PublusherDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Publusher
    success_url = reverse_lazy('manuals:publishers-list')
    login_url = '/accounts/login/'
    permission_required = ('dictionaries.delete_publusher')



