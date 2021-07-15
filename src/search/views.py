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

        # question = request.GET.get('q')
        # print(question)
        # if question is not None:
        #     search_books = Book.objects.filter(name__icontains=question)

        #     # формируем строку URL, которая будет содержать последний запрос
        #     # Это важно для корректной работы пагинации
        #     context['last_question'] = '?q=%s' % question

        #     current_page = Paginator(search_books, 2)

        #     page = request.GET.get('page')
        #     try:
        #         context['object_lists'] = current_page.page(page)
        #     except PageNotAnInteger:
        #         context['object_lists'] = current_page.page(1)
        #     except EmptyPage:
        #         context['object_lists'] = current_page.page(current_page.num_pages)
            
        #    # context['object_lists'] = search_books.all()

        # return render(request, template_name=self.template_name, context=context)

        q = request.GET.get('q')
        context['question'] = q 
        if q:
            query_sets = []  # Общий QuerySet
 
            # Ищем по всем моделям
            query_sets.append(Book.objects.filter(name__contains=q))
            query_sets.append(Author.objects.filter(name__contains=q))
            query_sets.append(BookGenre.objects.filter(name__contains=q))
            query_sets.append(BookSeries.objects.filter(name__contains=q))
            query_sets.append(Publusher.objects.filter(name__contains=q))

 
            # и объединяем выдачу
        #    final_set = list(chain(*query_sets))
            # final_set.sort(key=lambda x: x.pub_date, reverse=True)  # Выполняем сортировку
 
        #    context['last_question'] = '?q=%s' % q
 
            # current_page = Paginator(final_set, 10)
 
            # page = request.GET.get('page')
            # try:
            #     context['object_list'] = current_page.page(page)
            # except PageNotAnInteger:
            #     context['object_list'] = current_page.page(1)
            # except EmptyPage:
            #     context['object_list'] = current_page.page(current_page.num_pages)

            final_set = list(chain(*query_sets))
            context['object_lists'] = final_set 
            
 
        return render(request=request, template_name=self.template_name, context=context)