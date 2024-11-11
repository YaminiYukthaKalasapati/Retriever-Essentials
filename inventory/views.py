from django.shortcuts import render, redirect
from .models import InventoryItem
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django import forms
from .forms import InventoryItemForm
from django.contrib import messages
from django.contrib.auth import login, logout

def home(request):
    return render(request, 'inventory/home.html')  # Update the path

def blog(request):
    return render(request, 'inventory/blog.html')  # Update the path

def inventory(request):
    dairy_items = InventoryItem.objects.filter(category='Dairy')
    meat_items = InventoryItem.objects.filter(category='Meat')
    fruit_items = InventoryItem.objects.filter(category='Fruits')
    context = {
        'dairy_items': dairy_items,
        'meat_items': meat_items,
        'fruit_items': fruit_items,
    }
    return render(request, 'inventory/inventory.html', context)

def events(request):
    return render(request, 'inventory/events.html')  # Update the path

@login_required
def admin_page(request):
    return render(request, 'inventory/admin.html')  # Update the path

def search_inventory(request):
    query = request.GET.get('q')
    return render(request, 'inventory/search_results.html', {'query': query})

@login_required
def admin_dashboard(request):
    return render(request, 'inventory/admin_dashboard.html')

@login_required
def add_inventory(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item added successfully!')
            return redirect('inventory')  # Redirect to the inventory page after saving
    else:
        form = InventoryItemForm()

    return render(request, 'inventory/add_inventory.html', {'form': form})

def scan_barcode(request):
    barcode = request.GET.get('barcode')
    
    if barcode:
        # Check if item with this barcode already exists
        item, created = InventoryItem.objects.get_or_create(barcode=barcode, defaults={'name': 'New Item'})
        
        if created:
            message = 'New item added with barcode: ' + barcode
        else:
            message = 'Item with barcode already exists: ' + barcode
        
        return JsonResponse({'status': 'success', 'message': message})
    
    return JsonResponse({'status': 'error', 'message': 'Barcode not provided'})
def get_item_details(request):
    barcode = request.GET.get('barcode')
    try:
        item = InventoryItem.objects.get(barcode=barcode)
        return JsonResponse({
            "status": "success",
            "item": {
                "name": item.name,
                "description": item.description,
                "quantity": item.quantity,
                "price": item.price,
                "category": item.category.id  # or item.category.name if it's a related model
            }
        })
    except InventoryItem.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Item not found"})
def custom_admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('custom_admin')  # Redirect to the custom dashboard after login
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'admin_login.html')

@login_required
def custom_admin_dashboard(request):
    # This view will serve as the main dashboard with options to add items and scan barcodes
    return render(request, 'admin.html')
class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'description', 'quantity', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }