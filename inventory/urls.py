# inventory/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('blog/', views.blog, name='blog'),  # Blog page URL
    path('inventory/', views.inventory, name='inventory'),  # Inventory page URL
    path('events/', views.events, name='events'),  # Events page URL
    path('admin-page/', views.admin_page, name='admin_page'),  # Admin page URL
    path('add-inventory/', views.add_inventory, name='add_inventory'),  # Add inventory page URL
    path('search/', views.search_inventory, name='search_inventory'),  # Search inventory URL
    path('scan-barcode/', views.scan_barcode, name='scan_barcode'),  # Scan barcode URL
    path('custom-admin-login/', views.custom_admin_login, name='custom_admin_login'),  # Custom admin login URL
    path('custom-admin-dashboard/', views.custom_admin_dashboard, name='custom_admin_dashboard'),  # Custom admin dashboard URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login URL
    path('scan-barcode/', views.scan_barcode, name='scan_barcode'),  # Barcode scanning URL
    path('get-item-details/', views.get_item_details, name='get_item_details'),
]

