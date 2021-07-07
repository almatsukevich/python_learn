from django.views.generic import DetailView, UpdateView, DeleteView, RedirectView
from django.views import View
from . import models
from books import models as books_models
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib.auth import get_user_model

# Create your views here.

class CartView(DetailView):
    template_name = "carts/cart-edit.html"
    model = models.Cart

    def get_object(self, queryset=None):
        # get cart
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_id, 
            defaults={},
        )
     
        if created:
            self.request.session['cart_id'] = cart.pk
            if self.request.user.is_authenticated:      
                cart.customer = self.request.user
                cart.save()
        # get book_in_cart
        book_id = self.request.GET.get('book_id')
        if book_id:
            book = books_models.Book.objects.get(pk=int(book_id))
                # необходимо обработать на предмет левого id
            book_in_cart, book_created = models.BooksInCart.objects.get_or_create(
                cart=cart,
                book=book, 
                defaults={
                    'unit_price': book.unit_price
                },
            )    
            if not book_created:
                # prod position in the cart
                q = book_in_cart.quantity + 1
                book_in_cart.quantity = q
            else:
                book_in_cart.unit_price = book.unit_price

            book_in_cart.save()
        return cart   
    
# class DeleteGoodInCartView(DeleteView):
#     model = models.BooksInCart
#     success_url = reverse_lazy('carts:cart-edit')

class DeleteGoodInCartView(RedirectView):
    model = models.BooksInCart
    success_url = reverse_lazy('carts:cart-edit')

    def get_redirect_url(self, *args, **kwargs):
        self.model.objects.get(pk=self.kwargs.get('pk')).delete()
        return self.success_url

class CartUpdate(View):
    def post(self, request):
        action = request.POST.get('submit')
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_id,  
            defaults={},
        )      
        if created:
            self.request.session['cart_id'] = cart.pk

        goods = cart.goods.all()
        if goods:
            for key, value in request.POST.items():
                if 'quantityforgood_' in key:
                    pk = int(key.split('_')[1])
                    good = goods.get(pk=pk)
                    good.quantity = int(value)
                    good.save()
                    cart.save()

        if action == 'save_cart':
            return HttpResponseRedirect(reverse_lazy('carts:cart-edit'))

        elif action == 'create_order':
            return HttpResponseRedirect(reverse_lazy('orders:create-order'))
        else:
            return HttpResponseRedirect(reverse_lazy('carts:cart-edit'))