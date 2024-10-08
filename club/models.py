from django.db import models
from django_jalali.db import models as jmodels


# Create your models here.
class Customer(models.Model):
    class CustomerKind(models.TextChoices):
        NORMAL = 'NORMAL', 'مشتری معمولی'
        KNOWN = 'KNOWN', 'مشتری آشنا'
        LOYAL = 'LOYAL', 'مشتری وفادار'

    first_name = models.CharField(max_length=100, default='', verbose_name='نام')
    last_name = models.CharField(max_length=100, default='', verbose_name='نام خانوادگی')
    phone = models.CharField(max_length=11, verbose_name='شماره تلفن')
    register_date = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ پیوستن')
    last_visit_date = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین مراجه')
    visit_count = models.PositiveIntegerField(default=0, verbose_name='تعداد مراجعه')
    kind = models.CharField(max_length=6, choices=CustomerKind.choices, default=CustomerKind.NORMAL, verbose_name='نوع')

    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
        ordering = ['-register_date']
        indexes = [
            models.Index(fields=['phone', '-register_date'])
        ]

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
