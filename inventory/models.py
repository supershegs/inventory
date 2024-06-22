from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    contact_information = models.TextField()
    def __str__(self) -> str:
        return self.name
class Item(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    suppliers = models.ManyToManyField(Supplier, through='ItemSupplier')
    
    def __str__(self) -> str:
        return self.name




class ItemSupplier(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.supplier.name} supplies {self.item.name}"
    