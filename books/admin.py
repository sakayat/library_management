from django.contrib import admin
from .models import BooksModel, CommentModel

# Register your models here.
admin.site.register(BooksModel)
admin.site.register(CommentModel)