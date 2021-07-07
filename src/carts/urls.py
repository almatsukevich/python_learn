from django.urls import path
from carts import views 
app_name = 'carts'

urlpatterns = [
    path('cart-edit', views.CartView.as_view(), name = "cart-edit"),
    path('delete-good-in-cart/<int:pk>/', views.DeleteGoodInCartView.as_view(), name = "delete-good-in-cart"),
    path('update-cart/', views.CartUpdate.as_view(), name = "update-cart"),
]