from django.urls import path
from .views.supplier import (
    SupplierListView,
    SupplierDetailView
    
)




urlpatterns = [
    path('suppliers', SupplierListView.as_view()),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),

    
]