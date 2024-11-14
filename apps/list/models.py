from django.db import models

from apps.common.models import BaseModel
from apps.product.models import Product


class ListToBuy(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='list_to_buy')
    amount = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    where_to_buy = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.product.name

    @property
    def total_price(self):
        return self.price * self.amount
