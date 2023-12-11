from django.db import models

class Employee_detail(models.Model):
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    designation = models.CharField(max_length=100)
    empnumber = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    experiance = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    pastexp = models.BooleanField()
    prevjoin = models.CharField(max_length=100)
    prevleave = models.CharField(max_length=100)

    def __str__(self):
        return self.name