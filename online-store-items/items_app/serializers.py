from rest_framework import serializers
from items_app.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'amount', 'price', 'category', 'uuid', 'image', 'brand', 'color']

    def create(self, validated_data):
        new = Item(**validated_data)
        new.save()
        return new