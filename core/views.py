from django.views.generic import TemplateView
from books.models import BooksModel

# Create your views here.
class HomeTemplateView(TemplateView):
    model = BooksModel
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["books"] = BooksModel.objects.all()
        return context