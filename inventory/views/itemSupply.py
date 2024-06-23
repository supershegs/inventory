from typing import Optional

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from ..serializers import ItemSupplierSerializer, ItemSerializer


from ..models import (
    ItemSupplier, 
    Item,
    Supplier
)

from ..utils import (
    SuccessApiResponse,
    FailureApiResponse
)

class ItemSupplierListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request: HttpRequest, format: Optional[str] = None) -> HttpResponse:
        try:
            item_suppliers = ItemSupplier.objects.all()
            serializer = ItemSupplierSerializer(item_suppliers, many =True)
            if serializer.data == [] or serializer.data == '':
                return FailureApiResponse(msg="There are no Items  with supplier in the Inventory list.", status=status.HTTP_404_NOT_FOUND)
            return SuccessApiResponse(msg='Supplier item successfully fetched', data= serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
                print(f"line 22 {ex}")
                return FailureApiResponse(msg="Failed.", status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request: HttpRequest, format: Optional[str] = None) -> HttpResponse:
        serializer = ItemSupplierSerializer(data=request.data)
        if serializer.is_valid():
            try: 
                serializer.save()
                return SuccessApiResponse(msg='Supplier Item successfully created', data= serializer.data, status=status.HTTP_201_CREATED)
            except Exception as ex:
                print(f"line 22 {ex}")
                return FailureApiResponse(msg="Failed", errors=str(ex), status=status.HTTP_400_BAD_REQUEST)
        return FailureApiResponse(msg="Failed to add item, add missing fields", errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ItemSupplierDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request: HttpRequest, pk: int, format: Optional[str] = None) -> HttpResponse:
        try:
            item = Item.objects.get(pk=pk)
            relate_item_supplier = ItemSupplier.objects.filter(item=item)
            serializer = ItemSupplierSerializer(relate_item_supplier, many=True)
            return SuccessApiResponse(msg='Supplier item successfully fetched', data= serializer.data, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return FailureApiResponse(msg="No item in the Inventory list belong to the supplier.", status=status.HTTP_404_NOT_FOUND)
                                             
    
    
    def post(self, request: HttpRequest, pk: int,format: Optional[str] = None) -> HttpResponse:
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return FailureApiResponse(msg="Item not found ", status=status.HTTP_404_NOT_FOUND)

        supplier_ids = request.data.get("supplier_ids", [])
        if supplier_ids == [] or supplier_ids == '':
            return FailureApiResponse(msg="failed, add missing fields", errors='Enter a supplier ID', status=status.HTTP_400_BAD_REQUEST)
        for supplier_id in supplier_ids:
            try:
                supplier = Supplier.objects.get(pk=supplier_id)
            except Supplier.DoesNotExist:
                return FailureApiResponse(msg="suplier not found", status=status.HTTP_404_NOT_FOUND)

            if not ItemSupplier.objects.filter(item=item, supplier=supplier).exists():
                relate_item_supplier = ItemSupplier.objects.create(item=item, supplier=supplier)
    
        relate_item_supplier = ItemSupplier.objects.filter(item=item)
        serializer = ItemSupplierSerializer(relate_item_supplier, many=True)
        return SuccessApiResponse(msg='Supplier Item successfully created', data= serializer.data, status=status.HTTP_201_CREATED)
            
 
    def delete(self, request: HttpRequest, pk: int, format: Optional[str] = None) -> HttpResponse:
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return FailureApiResponse(msg="supplier not found", status=status.HTTP_404_NOT_FOUND)

        item_id = request.data.get('item_id', "")  
        if item_id == [] or item_id == '':
            return FailureApiResponse(msg="failed, add missing fields", errors='Enter an item_id', status=status.HTTP_400_BAD_REQUEST)  
        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            return FailureApiResponse(msg="Item not found on the inventory list", status=status.HTTP_404_NOT_FOUND)
        try:
            relate_item_supplier = ItemSupplier.objects.get(supplier=supplier, item=item)
        except ItemSupplier.DoesNotExist:
            return FailureApiResponse(msg="Supplier doesn't supply this item", status=status.HTTP_404_NOT_FOUND)
        relate_item_supplier.delete()
        return SuccessApiResponse(msg='Supplier Item successfully deleted', status=status.HTTP_200_OK)
        