from django.shortcuts import render, get_object_or_404, redirect
from IMS_app.models import Department, EmployeeDetail, Product, EmployeeProduct
from .forms import DepartmentForm, EmployeeDetailForm, ProductForm, EmployeeProductForm

def base(request):
    return render(request, 'base.html')
# Department Views
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'department_detail.html', {'department': department})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            department = form.save()
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department_form.html', {'form': form})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'department_confirm_delete.html', {'department': department})

# EmployeeDetail Views
def employee_detail_list(request):
    employees = EmployeeDetail.objects.all()
    return render(request, 'employee_detail_list.html', {'employees': employees})

def employee_detail_detail(request, pk):
    employee_detail = get_object_or_404(EmployeeDetail, pk=pk)
    return render(request, 'employee_detail_detail.html', {'employee_detail': employee_detail})


def employee_detail_create(request):
    if request.method == 'POST':
        form = EmployeeDetailForm(request.POST)
        if form.is_valid():
            employee = form.save()
            return redirect('employee_detail_detail', pk=employee.pk)
    else:
        form = EmployeeDetailForm()
    return render(request, 'employee_detail_form.html', {'form': form})

def employee_detail_update(request, pk):
    employee = get_object_or_404(EmployeeDetail, pk=pk)
    if request.method == 'POST':
        form = EmployeeDetailForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            return redirect('employee_detail_detail', pk=employee.pk)
    else:
        form = EmployeeDetailForm(instance=employee)
    return render(request, 'employee_detail_form.html', {'form': form})

def employee_detail_delete(request, pk):
    employee = get_object_or_404(EmployeeDetail, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_detail_list')
    return render(request, 'employee_detail_delete.html', {'employee': employee})

# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

# EmployeeProduct Views
def employee_product_list(request):
    employee_products = EmployeeProduct.objects.all()
    return render(request, 'employee_product_list.html', {'employee_products': employee_products})

def employee_product_detail(request, pk):
    employee_product = get_object_or_404(EmployeeProduct, pk=pk)
    return render(request, 'employee_product_detail.html', {'employee_product': employee_product})

def employee_product_create(request):
    if request.method == 'POST':
        form = EmployeeProductForm(request.POST)
        if form.is_valid():
            employee_product = form.save()
            return redirect('employee_product_detail', pk=employee_product.pk)
    else:
        form = EmployeeProductForm()
    return render(request, 'employee_product_form.html', {'form': form})

def employee_product_update(request, pk):
    employee_product = get_object_or_404(EmployeeProduct, pk=pk)
    if request.method == 'POST':
        form = EmployeeProductForm(request.POST, instance=employee_product)
        if form.is_valid():
            employee_product = form.save()
            return redirect('employee_product_detail', pk=employee_product.pk)
    else:
        form = EmployeeProductForm(instance=employee_product)
    return render(request, 'employee_product_form.html', {'form': form})

def employee_product_delete(request, pk):
    employee_product = get_object_or_404(EmployeeProduct, pk=pk)
    if request.method == 'POST':
        employee_product.delete()
        return redirect('employee_product_list')
    return render(request, 'employee_product_confirm_delete.html', {'employee_product': employee_product})

