from django.db import models

class Register(models.Model):
    email =  models.CharField(max_length=100)
    pwd =  models.CharField(max_length=100)
    fname = models.CharField(max_length=100) 
    lname =  models.CharField(max_length=100)
    phone =  models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    allergies =  models.CharField(max_length=100)
    address = models.CharField(max_length=100) 