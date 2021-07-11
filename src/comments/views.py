from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from . import forms, models
from django.urls import reverse_lazy

class CommentCreateView(FormView):
    form_class = forms.CommentCreateForm

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        next_step = form.cleaned_data.get('next_step')
        comment_text = form.cleaned_data.get('comment_text')
        author = self.request.user
        content_type_id = form.cleaned_data.get('content_type_id')
        object_id = form.cleaned_data.get('object_id')
        content_type = ContentType.objects.get_for_id(content_type_id)
        comment = models.Comment.objects.create(
            author=author,
            comment_text=comment_text,
            content_type=content_type,
            object_id=object_id
        )
        return HttpResponseRedirect(next_step)

