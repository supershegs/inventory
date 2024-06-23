from rest_framework import serializers

from .models import (
    Supplier, 
    Item, 
    ItemSupplier
)



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'date_created', 'date_updated']
        extra_kwargs = {
            'name': {'max_length': 300, 'min_length': 1, 'required': True},
            'description': {'min_length': 1, 'required': True}

        }

class SupplierSerializer(serializers.ModelSerializer):
    # items_supplied = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
    items_supplied = ItemSerializer(many=True, required=False)
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_information', 'items_supplied']
        extra_kwargs = {
            'name': {'max_length': 300, 'min_length': 2, 'required': True},
            'contact_information': {'min_length': 1, 'required': True}
        }
    def  create(self, validated_data):
        items_supplied_data = validated_data.pop('items_supplied', [])
        supplier = Supplier.objects.create(**validated_data)
        for item_data in items_supplied_data:
            item, _ = Item.objects.get_or_create(**item_data)
            ItemSupplier.objects.create(item=item, supplier=supplier)
        return supplier

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.contact_info = validated_data.get('contact_information', instance.contact_information)
        # items_supplied_data = validated_data.get('items_supplied', [])

        # instance.items_supplied.clear()
        # for item_data in items_supplied_data:
        #     item, _ = Item.objects.get_or_create(**item_data)
        #     ItemSupplier.objects.create(item=item, supplier=instance)

        # instance.save()
        return instance


class ItemSupplierSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    supplier = SupplierSerializer()
    class Meta:
        model = ItemSupplier
        fields = ['id', 'item', 'supplier']
