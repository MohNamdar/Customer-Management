from django.contrib import admin
from .models import Customer


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('phone', 'last_name', 'first_name', 'register_date', 'visit_count', 'kind')
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('phone', 'register_date', 'last_visit_date', 'kind')
