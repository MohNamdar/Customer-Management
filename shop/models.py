from django.db import models
from django_jalali.db import models as jmodels


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام دسته بندی')
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='دسته بندی')
    cover = models.ImageField(upload_to='shop/product_images/%Y/%m/', blank=True, null=True, verbose_name='تصویر')
    slug = models.SlugField(max_length=255, unique=True)
    real_price = models.PositiveIntegerField(verbose_name='قیمت اصلی')
    price = models.PositiveIntegerField(verbose_name='قیمت بعد از تخفیف')
    created = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['name']),
        ]
