from django.contrib import admin

# Register your models here.
from .models import (
    Supplier,
    Item,
    ItemSupplier
)



# admin.site.register(Config)
admin.site.register(Supplier)
admin.site.register(Item)
admin.site.register(ItemSupplier)