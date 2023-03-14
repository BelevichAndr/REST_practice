from django.urls import path

from orders.views import CutomerView, CutomerDetailView, OrderView, OrderDetail, ItemListView, ItemDetailView

app_name = "orders"

urlpatterns = [
    path('customers/', CutomerView.as_view(), name="customers_list"),
    path('customers/<int:pk>/',CutomerDetailView.as_view(),name="customer_detail"),
    path('orders/', OrderView.as_view(), name="orders_list"),
    path('orders/<int:pk>/', OrderDetail.as_view(), name="orders_detail"),
    path('items/', ItemListView.as_view(), name="items_list"),
    path('items/<slug:slug>', ItemDetailView.as_view(), name="items_detail"),
]
