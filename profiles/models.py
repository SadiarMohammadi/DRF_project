from django.db import models

# Create your models here.
class Profiles(models.Model):
    phone_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.phone_number}'
