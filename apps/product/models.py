from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    @property
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100" height="100" />')
        return 'No Image'

    @property
    def final_price(self):
        return self.discount_price if self.discount_price else self.price

    @property
    def discount_percent(self):
        if self.discount_price:
            return round((self.price - self.discount_price) / self.price * 100)
        return 0


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product.name

    @property
    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="100" height="100" />')


class Rate(models.Model):
    RATE = (
        (1, 'Very Bad'),
        (2, 'Bad'),
        (3, 'Normal'),
        (4, 'Good'),
        (5, 'Very Good'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rates')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='rates')
    rate = models.IntegerField(choices=RATE, default=3)

    def __str__(self):
        return f'{self.product} - {self.rate}'
