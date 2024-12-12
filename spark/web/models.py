from django.db import models

# Create your models here.
class Person(models.Model):
    # display person name in terminal using command
    # def __str__(self):
    #     return self.person_name 
    person_name = models.CharField( max_length= 100)
    person_age = models.IntegerField(default=25)
    person_num = models.IntegerField() 
    person_address = models.TextField(null = True, blank = False )

