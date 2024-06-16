from django.db import models
from books.models import BooksModel
from django.contrib.auth.models import User


# Create your models here.
class ReviewModel(models.Model):
    book = models.ForeignKey(
        BooksModel, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.content