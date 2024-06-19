from django.views.generic import TemplateView, DetailView
from books.models import BooksModel

# Create your views here.
class HomeTemplateView(TemplateView):
    model = BooksModel
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["books"] = BooksModel.objects.all()
        return context
    
class BookDetailsView(DetailView):
    model = BooksModel
    template_name = "book_details.html"
    pk_url_kwarg = "id"
    context_object_name = "book"
    

    