from django.urls import path

from .views import (
    department_list,
    department_detail,
    department_create,
    department_update,
    department_delete,
    employee_detail_list,
    employee_detail_detail,
    employee_detail_create,
    employee_detail_update,
    employee_detail_delete,
    product_list,
    product_detail,
    product_create,
    product_update,
    product_delete,
    employee_product_list,
    employee_product_detail,
    employee_product_create,
    employee_product_update,
    employee_product_delete,
)

urlpatterns = [
    path('departments/', department_list, name='department_list'),
    path('departments/create/', department_create, name='department_create'),
    path('departments/<int:pk>/', department_detail, name='department_detail'),
    path('departments/<int:pk>/update/', department_update, name='department_update'),
    path('departments/<int:pk>/delete/', department_delete, name='department_delete'),

    path('employees/', employee_detail_list, name='employee_detail_list'),
    path('employees/create/', employee_detail_create, name='employee_detail_create'),
    path('employees/<int:pk>/', employee_detail_detail, name='employee_detail_detail'),
    path('employees/<int:pk>/update/', employee_detail_update, name='employee_detail_update'),
    path('employees/<int:pk>/delete/', employee_detail_delete, name='employee_detail_delete'),

    path('products/', product_list, name='product_list'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/update/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),

    path('employee-products/', employee_product_list, name='employee_product_list'),
    path('employee-products/create/', employee_product_create, name='employee_product_create'),
    path('employee-products/<int:pk>/', employee_product_detail, name='employee_product_detail'),
    path('employee-products/<int:pk>/update/', employee_product_update, name='employee_product_update'),
    path('employee-products/<int:pk>/delete/', employee_product_delete, name='employee_product_delete'),
]


