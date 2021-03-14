from django.db import models

class Employee(models.Model):
    Eno         = models.AutoField(primary_key=True)
    Ename       = models.CharField(max_length=30)
    Esalary     = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return str(self.Eno)
