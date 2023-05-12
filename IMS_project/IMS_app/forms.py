# forms.py

from django import forms
from .models import Department, EmployeeDetail, Product, EmployeeProduct

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name',)

class EmployeeDetailForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = ('employee_code', 'name', 'number', 'email', 'address', 'city', 'age', 'department_name')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_tag', 'product_type', 'quantity', 'purchase_date')

class EmployeeProductForm(forms.ModelForm):
    class Meta:
        model = EmployeeProduct
        fields = ('employee_code', 'product_tag', 'quantity', 'date')
