from rest_framework import serializers

from .models import (
    Supplier, 
    Item, 
    ItemSupplier
)

# class SupplierSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=300, min_length= 1, required= True)
#     contact_information = serializers.CharField(min_length= 1,required= True)

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_information']
        extra_kwargs = {
            'name': {'max_length': 300, 'min_length': 2, 'required': True},
            'contact_information': {'min_length': 1, 'required': True}
        }
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'date_created', 'date_updated', 'suppliers']
        extra_kwargs = {
            'name': {'max_length': 300, 'min_length': 1, 'required': True},
        }

class ItemSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSupplier
        fields = ['id', 'item', 'supplier', 'contract_details', 'price_agreement']
