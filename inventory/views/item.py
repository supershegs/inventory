from typing import Optional

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from ..serializers import (
    SupplierSerializer,
    ItemSerializer,
    ItemSupplierSerializer
)

from ..models import (
    Supplier,
    Item,
    ItemSupplier
)
from ..utils import (
    SuccessApiResponse,
    FailureApiResponse
)


class ItemList(APIView):
    pass