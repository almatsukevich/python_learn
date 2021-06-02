from django import forms

from . import models

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = (
            'name',
            'desription'
        )

class CreateBookSeriesForm(forms.ModelForm):
    class Meta:
        model = models.BookSeries
        fields = (
            'name',
            'desription'
        )

class CreateBookGenreForm(forms.ModelForm):
    class Meta:
        model = models.BookGenre
        fields = (
            'name',
            'desription'
        )

class CreatePublusherForm(forms.ModelForm):
    class Meta:
        model = models.Publusher
        fields = (
            'name',
            'desription'
        )