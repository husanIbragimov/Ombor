from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Currency(BaseModel):
    usd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    usz = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"USD: {self.usd}, USZ: {self.usz}"
