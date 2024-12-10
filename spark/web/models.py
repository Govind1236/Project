from django.db import models

# Create your models here.
class Person(models.Model):
    person_name = models.CharField( max_length= 100),
    person_age = models.IntegerField(),
    person_num = models.IntegerField()
