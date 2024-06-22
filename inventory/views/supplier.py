from typing import Optional

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from ..serializers import SupplierSerializer


from ..models import Supplier
 
from ..utils import (
    SuccessApiResponse,
    FailureApiResponse
)

class SupplierListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request: HttpRequest, format: Optional[str] = None) -> HttpResponse:
        try:
            suppliers = Supplier.objects.all()
            serializer = SupplierSerializer(suppliers, many=True)
            print('Suppliers list on db: ',serializer.data)
            return SuccessApiResponse(msg='Suppliers successfully fetched', data= serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
                print(f"line 22 {ex}")
                return FailureApiResponse(msg="No Supplier yet.", status=status.HTTP_400_BAD_REQUEST)
        
        
    def post(self, request: HttpRequest, format: Optional[str] = None) -> HttpResponse:
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            try: 
                serializer.save()
                return SuccessApiResponse(msg='Supplier successfully created', data= serializer.data, status=status.HTTP_201_CREATED)
            except Exception as ex:
                print(f"line 22 {ex}")
                return FailureApiResponse(msg="Failed", errors=str(ex), status=status.HTTP_400_BAD_REQUEST)
        return FailureApiResponse(msg="Failed to add, add missing fields", errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SupplierDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request: HttpRequest, pk: int, format: Optional[str] = None) -> HttpResponse:
        try:
            supplier = get_object_or_404(Supplier, pk = pk)
            serializer = SupplierSerializer(supplier)
            print('Suppliers list on db: ',serializer.data)
            return SuccessApiResponse(msg='Suppliers successfully fetched', data= serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
                print(f"line 22 {ex}")
                return FailureApiResponse(msg="No Supplier matches the given query.", status=status.HTTP_404_NOT_FOUND)
            
    def put(self, request: HttpRequest, pk: int, format: Optional[str] = None) -> HttpResponse:
        try:
            supplier = get_object_or_404(Supplier, pk = pk)
            serializer = SupplierSerializer(supplier, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessApiResponse(msg='Supplier successfully modify', data= serializer.data, status=status.HTTP_200_OK)
            return FailureApiResponse(msg="Failed to modify, add missing fields", errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(f"line 22 {ex}")
            return FailureApiResponse(msg="Failed", errors=str(ex),status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request: HttpRequest, pk: int, format: Optional[str] = None) -> HttpResponse:
        try:
            supplier = get_object_or_404(Supplier,pk = pk)
            supplier.delete()
            return SuccessApiResponse(msg='Supplier successfully deleted', status=status.HTTP_200_OK)
        except Exception as ex:
            print(f"line 22 {ex}")
            return FailureApiResponse(msg="Failed", errors=str(ex), status=status.HTTP_404_NOT_FOUND)
    
    
            
    
        


