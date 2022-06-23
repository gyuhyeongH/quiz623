from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item,Category,Order
from .serializer import ItemSerializer
# Create your views here.


class ItemView(APIView):
    def get(self, request, category):
        category = Category.objects.filter(name=category)
        items = Item.objects.filter(category=category.id)

        data = ItemSerializer(items, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        item_serializer = ItemSerializer(data=request.data)

        if item__serializer.is_valid():
            item_serializer.save()
            return Response(item_serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderView(APIView):
    def get(self, request,order_id):
        orders = Order.objects.filter(id=order_id)
        data = ProductSerializer(orders, many=True).data
        return Response(data, status=status.HTTP_200_OK)
