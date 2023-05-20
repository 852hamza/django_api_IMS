# forms.py

from django import forms
from .models import Team, EmployeeDetail, Product, EmployeeProduct

class teamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name',)

class EmployeeDetailForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = ('employee_code', 'name', 'number', 'email', 'address', 'city','designation', 'age', 'team')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_tag', 'product_type','manufacture_by', 'product_capacity','quantity', 'purchase_date')

class EmployeeProductForm(forms.ModelForm):
    class Meta:
        model = EmployeeProduct
        fields = ('employee_code', 'product_tag', 'quantity', 'issue_date','assign_by','status')
