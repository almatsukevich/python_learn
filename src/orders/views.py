from . import models, forms
from django.views.generic import FormView, DetailView, ListView, UpdateView
from carts.models import Cart, BooksInCart
from books.models import Book
from dictionaries.models import Status
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.

class CreateOrderView(FormView):
    form_class = forms.OrderCreateForm
    template_name = 'orders/create-order.html'
#    success_url = reverse_lazy('orders:success')

    def get_initial(self):
        if self.request.user.is_anonymous:
            return {}
        name = self.request.user.first_name
        phone = self.request.user.profile.phone
        info = str(self.request.user.profile.index) + ', ' + \
        str(self.request.user.profile.country) + ', ' + \
        str(self.request.user.profile.city) + ', ' + \
        str(self.request.user.profile.address1)
        return {
            'customer_name' : name,
            'customer_phone' : phone,
            'contact_info' : info
            }

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        cart, created = Cart.objects.get_or_create(
            pk=cart_id,  
            defaults={},
        )      
        if created:
            return HttpResponseRedirect(reverse_lazy('carts:cart-edit'))
        c_info = form.cleaned_data.get('contact_info')
        c_name = form.cleaned_data.get('customer_name')
        c_phone = form.cleaned_data.get('customer_phone')
        order = models.Order.objects.create(
            cart=cart,
            contact_info=c_info,
            customer_name=c_name,
            customer_phone=c_phone
        )
        goods_in_cart = BooksInCart.objects.filter(cart=cart)
        for good in goods_in_cart:
            book_pk = good.book.pk
            book_quantity = good.quantity
            b = Book.objects.get(pk=book_pk)
            b.quantity -= book_quantity
            b.num_orders += book_quantity
            if b.quantity == 0:
                b.active = False
            b.save()
               

        del self.request.session['cart_id']
        return HttpResponseRedirect(reverse_lazy('orders:orders-list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        cart, created = Cart.objects.get_or_create(
            pk=cart_id,  
            defaults={},
        )
        context['object'] = cart
        return context

class OrderDetailView(DetailView):
    model = models.Order

class OrderListView(ListView):
    model = models.Order
    paginate_by = 10

    def get_queryset(self):
        qs=super().get_queryset()
        filter = self.request.GET.get('filter')
        if filter == 'new':
            qs = qs.filter(status__pk=1)
        if filter == 'processed':
            qs = qs.filter(status__pk=2)
        if filter == 'go':
            qs = qs.filter(status__pk=3)
        if filter == 'ok':
            qs = qs.filter(status__pk=4)
        if filter == 'cancel':
            qs = qs.filter(status__pk=5)
        
        if self.request.user.groups.filter(name='Managers').exists():
            return qs.order_by('-created')
        if self.request.user.is_authenticated:
            user_now = self.request.user
            return qs.filter(cart__customer=user_now).order_by('-created')
        else:
            return qs.filter(pk=0)


class OrderUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.Order
    form_class = forms.OrderUpdateForm
    success_url = reverse_lazy('orders:orders-list')
    login_url = '/accounts/login/'
    permission_required = ('orders.change_order')

    def form_valid(self, form):
        status_pk = int(self.request.POST.get(key='status'))
        customer_name = self.request.POST.get(key='customer_name')
        customer_phone = self.request.POST.get(key='customer_phone')
        contact_info = self.request.POST.get(key='contact_info')
      
        order = models.Order.objects.filter(pk=self.kwargs.get('pk')).update(
            status=Status.objects.get(pk=status_pk), 
            customer_name=customer_name, 
            customer_phone=customer_phone, 
            contact_info=contact_info,
            manager = self.request.user
            )
        order = models.Order.objects.get(pk=self.kwargs.get('pk'))
        print(order)
        if status_pk == 5:
            goods_in_cart = BooksInCart.objects.filter(cart=order.cart)
            for good in goods_in_cart:
                book_pk = good.book.pk
                book_quantity = good.quantity
                b = Book.objects.get(pk=book_pk)
                b.quantity += book_quantity
                if b.quantity > 0:
                    b.active = True
                b.num_orders -= book_quantity
                b.save()
        return HttpResponseRedirect(reverse_lazy('orders:orders-list'))
       