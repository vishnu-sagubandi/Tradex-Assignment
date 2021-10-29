from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150)
    weight = models.CharField(max_length=50)
    price = models.DecimalField(_(u'Price(in rupees)'), decimal_places=2, max_digits=12, validators=[
                                MinValueValidator(Decimal('0.01'))])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
