from django.db import models
from django.contrib.auth.models import User
from .constants import transactions_type


# Create your models here.
class TransactionsModel(models.Model):
    account = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions"
    )
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0.0)
    balance_after_purchase = models.DecimalField(
        decimal_places=2, max_digits=12, null=True
    )
    transactions_type = models.IntegerField(choices=transactions_type, null=True, blank=True)
    return_book = models.BooleanField(default=False)
    
    
    
    def __str__(self):
        return self.account