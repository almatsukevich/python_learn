from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View

from books.models import Book

from dictionaries.models import Author, BookGenre, BookSeries, Publusher
from itertools import chain

class ESearchView(View):
    template_name = 'search/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        q = request.GET.get('q')
        context['question'] = q 
        if q:
            query_sets = []  
            query_sets.append(Book.objects.filter(name__contains=q))
            query_sets.append(Author.objects.filter(name__contains=q))
            query_sets.append(BookGenre.objects.filter(name__contains=q))
            query_sets.append(BookSeries.objects.filter(name__contains=q))
            query_sets.append(Publusher.objects.filter(name__contains=q))

            final_set = list(chain(*query_sets))
            context['object_lists'] = final_set 
        return render(request=request, template_name=self.template_name, context=context)