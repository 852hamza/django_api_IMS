from django.urls import path
from . import views

urlpatterns = [
    # team URLs
    path('teams/', views.team_list, name='team_list'),
    path('teams/<int:pk>/', views.team_detail, name='team_detail'),
    path('teams/create/', views.team_create, name='team_create'),
    path('teams/<int:pk>/update/', views.team_update, name='team_update'),
    path('teams/<int:pk>/delete/', views.team_delete, name='team_delete'),
    
    # EmployeeDetail URLs
    path('employees/', views.employee_detail_list, name='employee_detail_list'),
    path('employees/<int:pk>/', views.employee_detail_detail, name='employee_detail_detail'),
    path('employees/create/', views.employee_detail_create, name='employee_detail_create'),
    path('employees/<int:pk>/update/', views.employee_detail_update, name='employee_detail_update'),
    path('employees/<int:pk>/delete/', views.employee_detail_delete, name='employee_detail_delete'),
    
    # Product URLs
    path('products/', views.product_list, name='product_list'),
    path('products/<str:pk>//', views.product_detail, name='product_detail'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<str:pk>/update/', views.product_update, name='product_update'),
    path('products/<str:pk>/delete/', views.product_delete, name='product_delete'),
    
    # EmployeeProduct URLs
    path('employee-products/', views.employee_product_list, name='employee_product_list'),
    path('employee-products/<int:pk>/', views.employee_product_detail, name='employee_product_detail'),
    path('employee-products/create/', views.employee_product_create, name='employee_product_create'),
    path('employee-products/<int:pk>/update/', views.employee_product_update, name='employee_product_update'),
    path('employee-products/<int:pk>/delete/', views.employee_product_delete, name='employee_product_delete'),

    # search url
    path('live-search/', views.live_search, name='live_search'),
    
    path('', views.home, name='home'),
]



