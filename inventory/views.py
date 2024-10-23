from django.shortcuts import render

def home(request):
    return render(request, 'inventory/home.html')  # Update the path

def blog(request):
    return render(request, 'inventory/blog.html')  # Update the path

def inventory(request):
    return render(request, 'inventory/inventory.html')  # Update the path

def events(request):
    return render(request, 'inventory/events.html')  # Update the path

def admin_page(request):
    return render(request, 'inventory/admin.html')  # Update the path

def search_inventory(request):
    query = request.GET.get('q')
    return render(request, 'inventory/search_results.html', {'query': query})

def add_inventory(request):
    return render(request, 'inventory/add_inventory.html')  # Update the path
