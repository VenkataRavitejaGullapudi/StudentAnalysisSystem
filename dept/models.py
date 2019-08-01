from django.db import models
# Create your models here.

class Dept(models.Model):
    dept_name=models.CharField(max_length=3)

class Subjects(models.Model):
    teac_id = models.IntegerField()
    sub_name=models.CharField(max_length=30)
    sub_code = models.CharField(max_length=10)
    dept_id=models.CharField(max_length=10)
    year=models.CharField(max_length=10)
    def __str__(self):
        return ('For Year-'+self.year+' & '+'For Dept-'+self.dept_id)