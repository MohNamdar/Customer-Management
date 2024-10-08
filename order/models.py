from django.db import models
from club.models import Customer
from shop.models import Product
from django_jalali.db import models as jmodels


# Create your models here.
class Order(models.Model):
    buyer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='orders', null=True,
                              verbose_name='خریدار')
    created = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]

    def __str__(self):
        return f"سفارش #{self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='سفارش')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name='محصول')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
