from django.db import models
#password ciao come va
# Create your models here.

class Person(models.Model):
    email_address = models.EmailField(max_length=70,blank=True)
    first_name = models.CharField(max_length=30)
    message = models.TextField(max_length=200)
    checkbox = models.BooleanField()

    def __str__(self):
       return 'Utente: ' + self.first_name


    