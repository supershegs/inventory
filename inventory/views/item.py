from typing import Optional

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from ..serializers import ItemSerializer


from ..models import Item

from ..utils import (
    SuccessApiResponse,
    FailureApiResponse
)


class ItemListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request: HttpRequest, format: Optional[str] = None) -> HttpResponse:
        try:
            items  = Item.objects.all()
            serializer = ItemSerializer(items, many =True)
            if serializer.data == [] or serializer.data == '':
                return FailureApiResponse(msg="There are no Items in the Inventory list.", status=status.HTTP_404_NOT_FOUND)
            return SuccessApiResponse(msg='items successfully fetched', data= serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
                print(f"line 22 {ex}")
                return FailureApiResponse(msg="Failed.", status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request: HttpRequest, format: Optional[str] = None) -> HttpResponse:
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            try: 
                serializer.save()
                return SuccessApiResponse(msg='Item successfully created', data= serializer.data, status=status.HTTP_201_CREATED)
            except Exception as ex:
                print(f"line 22 {ex}")
                return FailureApiResponse(msg="Failed", errors=str(ex), status=status.HTTP_400_BAD_REQUEST)
        return FailureApiResponse(msg="Failed to add item, add missing fields", errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class itemDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request: HttpRequest, pk: int, format: Optional[str] = None) -> HttpResponse:
        try:
            item = get_object_or_404(Item, pk =pk)
            serializer = ItemSerializer(item)
            return SuccessApiResponse(msg='item successfully fetched', data= serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            print(f"line 22 {ex}")
            return FailureApiResponse(msg="No item in the Inventory matches the given query.", status=status.HTTP_404_NOT_FOUND)
            
    def put(self, request: HttpRequest, pk: int, format: Optional[str] = None) -> HttpResponse:
        try:
            item = get_object_or_404(Item, pk =pk)
            serializer = ItemSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessApiResponse(msg='Item successfully modify', data= serializer.data, status=status.HTTP_200_OK)
            return FailureApiResponse(msg="Failed to modify item, add missing fields", errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(f"line 22 {ex}")
            return FailureApiResponse(msg="Failed", errors=str(ex),status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request: HttpRequest, pk: int, format: Optional[str] = None) -> HttpResponse:
        try:
            item = get_object_or_404(Item, pk=pk)
            item.delete()
            return SuccessApiResponse(msg='Item successfully deleted', status=status.HTTP_200_OK)
        except Exception as ex:
            print(f"line 22 {ex}")
            return FailureApiResponse(msg="Failed", errors=str(ex), status=status.HTTP_404_NOT_FOUND)
    