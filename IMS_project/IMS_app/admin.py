from django.contrib import admin
from .models import EmployeeDetail, Department, Product, EmployeeProduct
from .views import *

class EmployeeDetailAdmin(admin.ModelAdmin):
    list_display = ('employee_code', 'name', 'number', 'email', 'address', 'city', 'age', 'department_name')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_tag', 'product_type', 'quantity', 'purchase_date')

class EmployeeProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_code', 'product_tag', 'quantity', 'date')

admin.site.register(EmployeeDetail, EmployeeDetailAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(EmployeeProduct, EmployeeProductAdmin)

# CRUD views for EmployeeDetail
admin.site.add_action(employee_detail_create, name='Create Employee')
admin.site.add_action(employee_detail_update, name='Update Employee')
admin.site.add_action(employee_detail_delete, name='Delete Employee')

# CRUD views for Product
admin.site.add_action(product_create, name='Create Product')
admin.site.add_action(product_update, name='Update Product')
admin.site.add_action(product_delete, name='Delete Product')

# CRUD views for EmployeeProduct
admin.site.add_action(employee_product_create, name='Create Employee Product')
admin.site.add_action(employee_product_update, name='Update Employee Product')
admin.site.add_action(employee_product_delete, name='Delete Employee Product')
from django.contrib import admin

# Register your models here.
