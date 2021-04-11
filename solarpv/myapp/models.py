from django.db import models


# Create your models here.

class Appellation(models.Model):
    title = models.CharField(max_length=255)


class Company(models.Model):
    name = models.CharField(max_length=255)


class User(models.Model):
    username = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    appellation = models.ForeignKey(Appellation, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    office_phone = models.CharField(max_length=255)
    cell_phone = models.CharField(max_length=255)
