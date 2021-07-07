from django.urls import path
from orders import views 
app_name = 'orders'

urlpatterns = [
    path('create-order', views.CreateOrderView.as_view(), name = "create-order"),
    path('orders-list', views.OrderListView.as_view(), name = "orders-list"),
    path('<int:pk>/', views.OrderDetailView.as_view(), name = "order"),
    path('order-update/<int:pk>/', views.OrderUpdateView.as_view(), name = "order-update")
]