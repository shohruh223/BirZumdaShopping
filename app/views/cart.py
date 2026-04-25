from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from app.models import Cart, CartItem, Product


def get_active_cart(user):
    cart, created = Cart.objects.get_or_create(user=user, checked_out=False)
    return cart


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        cart = get_active_cart(request.user)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if created:
            item.quantity = 1
        else:
            item.quantity += 1
        item.save()

        return redirect('savatcha')


class SavatchaView(LoginRequiredMixin, TemplateView):
    template_name = 'savatcha.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user, checked_out=False).first()

        if cart:
            cart_items = cart.items.select_related('product').all()
            cart_total = cart.total_price
        else:
            cart_items = []
            cart_total = 0

        context['cart'] = cart
        context['cart_items'] = cart_items
        context['cart_total'] = cart_total
        return context
