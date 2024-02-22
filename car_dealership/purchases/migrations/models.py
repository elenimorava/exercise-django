from django.db import models
from car_dealership.customers.migrations.models import Customer
from car_dealership.autos.migrations.models import Auto
from car_dealership.dealers.migrations.models import Dealer

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Purchase of {self.auto} by {self.customer} from {self.dealer} on {self.purchase_date}"