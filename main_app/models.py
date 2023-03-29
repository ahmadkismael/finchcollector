from django.db import models
from django.urls import reverse



SERVICE = (
    ('O', 'Oil change'),
    ('T', 'Tire change'),
    ('C', 'Check up')
)

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.make
    
    def get_absolute_url(self):
        return reverse ('detail', kwargs={'car_id' : self.id})
    


class Updates(models.Model):
    date = models.DateField('service date')
    service = models.CharField(max_length=1, choices=SERVICE, default=SERVICE[0][0])
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"
    

    class Meta:
        ordering = ['-date']

