from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import TransactionsModel
# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    model = TransactionsModel
    success_url = reverse_lazy("home")
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"amount": self.request.user.account})
        return kwargs
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    