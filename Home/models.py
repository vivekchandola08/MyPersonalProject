from django.db import models


# 1. models register ----> In admin.py
# 2. app register ----->  In settings.py

# Create your models here.
class Contact(models.Model):                      #Contact -----> table
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    