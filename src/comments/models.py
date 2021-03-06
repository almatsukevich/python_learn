from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    comment_text = models.TextField(verbose_name="Текст комментария")
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True, auto_now=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')