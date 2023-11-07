from django.db import models

# Create your models here.


class Reservation(models.Model):
    user = models.CharField(max_length=200)
    site = models.CharField(max_length=150)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} , {self.checkin_date}-{self.checkout_date}: ${self.price}"

    def dates(self):
        return f"{self.checkin_date}-{self.checkout_date}"
