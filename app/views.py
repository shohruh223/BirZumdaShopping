from django.views.generic import TemplateView, ListView, DetailView

from app.models import Product


class IndexView(TemplateView):
    template_name = 'index.html'


class MahsulotlarView(ListView):
    template_name = 'mahsulotlar.html'
    # model = Product
    context_object_name = 'products'
    paginate_by = 4
    queryset = Product.objects.all()


class MahsulotlarDetailView(DetailView):
    template_name = 'mahsulot-detail.html'
    model = Product
    context_object_name = 'product'