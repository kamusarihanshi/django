from django.db import models

# Create your models here.
class Tour (models.Model):
    country = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()


    #string representation
    def __str__(self):
        return f"id:{self.id},from:{self.country} to {self.destination} price :{self.price}"