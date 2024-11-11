# syna_solutions/urls.py
from django.contrib import admin
from django.urls import path, include
from inventory import views  # Import views from inventory

urlpatterns = [
    path('admin/', admin.site.urls),  # Default Django admin page
    path('inventory/', include('inventory.urls')),  # Include all URLs from the inventory app
    path('', views.home, name='home'),  # Root URL set to the home view
]
