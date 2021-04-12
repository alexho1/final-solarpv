from django.db import models
from django.utils import text


# Create your models here.

class Appellation(models.Model):
    title = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['title']

        def __init__(self):
            self.title = None

        def __str__(self):
            return self.title


class Company(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, null=True)

    class Meta:
        ordering = ['name']

        def __init__(self):
            self.name = None

        def __str__(self):
            return self.name


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    appellation = models.ForeignKey(Appellation, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    office_phone = models.CharField(max_length=255)
    cell_phone = models.CharField(max_length=255)

    class Meta:
        ordering = ['username']

        def __init__(self):
            self.username = None

        def __str__(self):
            return self.username


class Certificate(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    issue_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['number']

        def __init__(self):
            self.number = None

        def __str__(self):
            return self.number
