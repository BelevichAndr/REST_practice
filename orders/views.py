from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView

from orders.serializers import (CustomerSerializer, OrderSerializer,
                                ShippingSerializer, ItemSerializer)
from orders.models import Order, Customer, Shipping, Item


class CutomerView(ListCreateAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    # def get(self, request):
    #   customers = Customer.objects.all()
    #   serializer = self.serializer_class(customers, many=True)
    #   return Response(serializer.data)

    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid(raise_exception=False):
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response({"error": "invalid data"})

    def delete(self, request):
        pk = request.data.get("pk")
        if not pk:
            return Response({"error": "invalid data"})
        else:
            try:
                obj = Customer.objects.get(pk=pk).delete()
                print(obj)
                return Response({"status": "OK"})
            except Customer.DoesNotExist:
                return Response({"error": "invalid pk"})

    # def get_paginated_response(self, data):
    #      return Response(data)


class CutomerDetailView(APIView):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ItemListView(ListCreateAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer


class ItemDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  # lookup_field = "slug"

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())
    slug = self.kwargs.get("slug")
    obj = get_object_or_404(queryset, slug=slug)  
    self.check_object_permissions(self.request, obj)

    return obj
     
