from django.db import models

# Create your models here.
class Person(models.Model):
    def __str__(self):
        return self.person_name
    
    person_name = models.CharField( max_length= 100)
    person_age = models.IntegerField(default=25)
    person_num = models.IntegerField() 
