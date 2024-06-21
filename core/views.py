from django.views.generic import TemplateView, DetailView, CreateView, FormView
from books.models import BooksModel
from category.models import CategoryModel
from books.forms import UserCommentFrom
from django.views.generic.edit import FormMixin
# Create your views here.
class HomeTemplateView(TemplateView):
    model = BooksModel
    template_name = "index.html"
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        category_slug = self.kwargs.get("cta_name")
        if category_slug:
            category = CategoryModel.objects.get(slug=category_slug)
            context["books"] = BooksModel.objects.filter(category=category)
        else:
            context["books"] = BooksModel.objects.all()
        context["categories"] = CategoryModel.objects.all()
        return context
    
class BookDetailsView(FormMixin, DetailView):
    model = BooksModel
    form_class = UserCommentFrom
    template_name = "book_details.html"
    pk_url_kwarg = "id"
    context_object_name = "book"
    
    



