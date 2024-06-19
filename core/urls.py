from django.urls import path
from .import views
urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
     path("book/<int:id>", views.BookDetailsView.as_view(), name="book_details"),
]
