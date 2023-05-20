from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q,Sum
from IMS_app.models import Team, EmployeeDetail, Product, EmployeeProduct
from .forms import teamForm, EmployeeDetailForm, ProductForm, EmployeeProductForm

# base view
def base(request):
    return render(request, 'base.html')

#  for collecting total data 
def home(request):
    total_employees = EmployeeDetail.objects.count()
    total_products = Product.objects.count()
    total_assigned_products = EmployeeProduct.objects.count()

    return render(request, 'home.html', {
        'total_employees': total_employees,
        'total_products': total_products,
        'total_assigned_products': total_assigned_products
    })
    
# # search bar
def live_search(request):
    query = request.GET.get('query', '')
    
    products = Product.objects.filter(
        Q(product_tag__icontains=query) |
        Q(manufacture_by__icontains=query) |
        Q(product_capacity__icontains=query) |
        Q(product_type__icontains=query)
    )
    
    employees = EmployeeDetail.objects.filter(
        Q(employee_code__icontains=query) |
        Q(name__icontains=query)
    )
    
    context = {
        'products': products,
        'employees': employees,
        'query': query
    }
    
    return render(request, 'live_search.html', context)
# team Views
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'team_detail.html', {'team': team})

def team_create(request):
    if request.method == 'POST':
        form = teamForm(request.POST)
        if form.is_valid():
            team = form.save()
            return redirect('team_detail', pk=team.pk)
    else:
        form = teamForm()
    return render(request, 'team_form.html', {'form': form})

def team_update(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = teamForm(request.POST, instance=team)
        if form.is_valid():
            team = form.save()
            return redirect('team_detail', pk=team.pk)
    else:
        form = teamForm(instance=team)
    return render(request, 'team_form.html', {'form': form})

def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'team_confirm_delete.html', {'team': team})

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
    total_quantity = products.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    assigned_quantity = EmployeeProduct.objects.aggregate(assigned_quantity=Sum('quantity'))['assigned_quantity']
    return render(request, 'product_list.html', {'products': products,'total_quantity': total_quantity,
        'assigned_quantity': assigned_quantity,})

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

