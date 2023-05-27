from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(default="", max_length=50)
    email = models.CharField(default="", max_length=50)
    phone = models.CharField(default="", max_length=50)
    
    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    def __str__(self):
        return self.name


class up_data(models.Model):
    file = models.FileField(upload_to="excel")