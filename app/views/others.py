from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from app.models import Product


class IndexView(TemplateView):
    template_name = 'index.html'


class MahsulotlarView(ListView):
    template_name = 'mahsulotlar.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        queryset = Product.objects.all()

        sort = self.request.GET.get('sort')
        if sort == 'price_asc':
            queryset = queryset.order_by('price')
        if sort == 'price_desc':
            queryset = queryset.order_by('-price')

        q = self.request.GET.get('q')

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q))

        return queryset


class MahsulotlarDetailView(DetailView):
    template_name = 'mahsulot-detail.html'
    model = Product
    context_object_name = 'product'