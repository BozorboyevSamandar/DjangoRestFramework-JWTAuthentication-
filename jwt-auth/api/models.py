from django.db import models


# Create your models here.


class Student(models.Model):
    id = models.IntegerField(primary_key=True,)
    last_name = models.CharField(max_length=500)
    first_name = models.CharField(max_length=500)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"