from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
    class Meta:
        app_label = 'IMS_app'

class EmployeeDetail(models.Model):
    employee_code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100, unique=True)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    designation = models.CharField(max_length=100, null=True )
    age = models.PositiveSmallIntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='employees')
    
    def __str__(self):
        return self.name 

    class Meta:
        app_label = 'IMS_app'
class Product(models.Model):
    product_tag = models.CharField(primary_key=True, max_length=15)
    product_type = models.CharField(max_length=50)
    manufacture_by = models.CharField(max_length=50, null=True )
    product_capacity = models.CharField(max_length=50, null=True )
    quantity = models.PositiveIntegerField()
    purchase_date = models.DateField()
    
    def __str__(self):
        return f"{self.product_type}"

    class Meta:
        app_label = 'IMS_app'
class EmployeeProduct(models.Model):
    employee_code = models.ForeignKey(EmployeeDetail, on_delete=models.CASCADE)
    product_tag = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    issue_date = models.DateField()
    assign_by= models.CharField(max_length=100, null=True )
    def __str__(self):
        return f"{self.employee_code} - {self.product_tag} - {self.quantity} - {self.issue_date}"
    class Meta:
        app_label = 'IMS_app'