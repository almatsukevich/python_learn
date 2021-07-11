from django.contrib import admin
from . import models

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'comment_text', 'created']


admin.site.register(models.Comment, CommentAdmin)