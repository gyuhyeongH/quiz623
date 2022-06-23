from rest_framework import serializers
from .models import Category
from .models import Item
from .models import Order
from .models import ItemOrder


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name"]


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ["name","category","image_url"]


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ["delivery_address","order_date","item"]


class ItemOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemOrder
        fields = ["order","item","item_count"]