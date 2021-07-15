from django import forms

from . import models

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
       # fields = '__all__'
        fields = [
            'name',
            'picture',
            'unit_price',
            'author',
            'serie',
            'genre',
            'year',
            'pages',
            'binding',
            'book_format',
            'isbn',
            'weight',
            'age_stop',
            'publusher',
            'quantity',
            'active',
            'rating'
        ]