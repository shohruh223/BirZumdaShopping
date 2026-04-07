from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import TemplateView, ListView, DetailView

from app.form import RegisterForm, EmailLoginForm
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


# ------------------------------------ Auth


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        super().form_valid(form)
        logout(self.request)
        return redirect("login")


class UserLoginView(LoginView):
    authentication_form = EmailLoginForm
    template_name = "login.html"
    redirect_authenticated_user = True


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")

    def post(self, request):
        logout(request)
        return redirect("login")
