from django.urls import path
from .import views

urlpatterns = [
    path("deposit/", views.DepositMoneyView.as_view(), name="deposit"),
    path("borrow_book/<int:book_id>", views.BorrowBookView.as_view(), name="borrow_book"),
]
