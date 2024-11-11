from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import InventoryItem
from .forms import InventoryItemForm

class InventoryItemAdmin(admin.ModelAdmin):
    form = InventoryItemForm

    class Media:
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/quagga/0.12.1/quagga.min.js',  # QuaggaJS for barcode scanning
            'js/barcode_scanner.js',  # Your custom JavaScript for initializing Quagga
        )

admin.site.register(InventoryItem, InventoryItemAdmin)
