from django.urls import path
from .views.supplier import (
    SupplierListView,
    SupplierDetailView,
    SupplierAddItemAPIView
)

from .views.item import (
    ItemListView,
    itemDetailView
)

from .views.itemSupply import (
    ItemSupplierListView,
    ItemSupplierDetailView
)




urlpatterns = [
    path('suppliers', SupplierListView.as_view()),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path("items", ItemListView.as_view() ),
    path('items/<int:pk>/', itemDetailView.as_view()),
    path('suppliers-items', ItemSupplierListView.as_view() ),
    path('suppliers-items/<int:pk>/', ItemSupplierDetailView.as_view() ),
    path('suppliers/add-item/<int:pk>/', SupplierAddItemAPIView.as_view())
    
]