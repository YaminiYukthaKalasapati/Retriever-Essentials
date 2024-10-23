from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('blog/', views.blog, name='blog'),  # Blog page
    path('inventory/', views.inventory, name='inventory'),  # Inventory page
    path('events/', views.events, name='events'),  # Events page
    path('admin/', views.admin_page, name='admin_page'),  # Admin page
    path('add-inventory/', views.add_inventory, name='add_inventory'),  # Add inventory page
    path('search/', views.search_inventory, name='search_inventory'),  # Search inventory page
]
