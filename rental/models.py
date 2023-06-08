from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Car(models.Model):
    
    GEARS = (
        (4, 'Manuel 4 Vites'),
        (5, 'Manuel 5 Vites'),
        (6, 'Manuel 6 Vites'),
        (7, 'Manuel 7 Vites'),
        (8, 'Manuel 8 Vites'),
        (1, 'Tam Otomatik Vites'),
        (2, 'Yarı Otomatik Vites'),        
    )
    
    plate_number = models.CharField(max_length=20)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    gear = models.PositiveSmallIntegerField(choices=GEARS)
    rent_per_day = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return f'[ {self.brand} {self.model} === {self.plate_number} ]'

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    TC_No = models.PositiveIntegerField(null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f'{self.car} [{self.customer}]  [ {self.start_date} ### {self.end_date} ]'

    def clean(self):
        # Check if the car is already reserved for the same date
        if Reservation.objects.filter(car=self.car, start_date__lte=self.end_date, end_date__gte=self.start_date).exists():
            raise ValidationError(_('The car is already reserved for the selected date.'))

        # Check if the customer has already reserved a car for the same date
        if Reservation.objects.filter(customer=self.customer, start_date__lte=self.end_date, end_date__gte=self.start_date).exists():
            raise ValidationError(_('You have already reserved a car for the selected date.'))
