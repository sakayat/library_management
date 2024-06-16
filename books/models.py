from django.db import models
from category.models import CategoryModel


# Create your models here.
class BooksModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    borrowing_price = models.DecimalField(decimal_places=2, max_digits=12)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    category = models.ForeignKey(
        CategoryModel, on_delete=models.CASCADE, related_name="books"
    )
    
    def __str__(self) -> str:
        return self.title