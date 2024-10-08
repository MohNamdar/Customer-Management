from django import forms
from .models import Order
from shop.models import Product
from club.models import Customer


class NewOrder(forms.ModelForm):
    buyer_phone = forms.CharField(max_length=11, label='شماره تلفن')
    first_name = forms.CharField(max_length=100, required=False, label='نام')
    last_name = forms.CharField(max_length=100, required=False, label='نام خانوادگی')

    class Meta:
        model = Order
        fields = []

    def __init__(self, *args, **kwargs):
        super(NewOrder, self).__init__(*args, **kwargs)
        # Dynamically add product selection fields
        products = Product.objects.all()
        for product in products:
            self.fields[f'product_{product.id}'] = forms.BooleanField(
                label=product.name, required=False,
            )
            self.fields[f'quantity_{product.id}'] = forms.IntegerField(
                min_value=1, required=False, label=""
            )

    def clean_buyer_phone(self):
        phone = self.cleaned_data.get('buyer_phone')
        if not phone.isdigit():
            raise forms.ValidationError('شماره تلفن باید بصورت عددی نوشته شود.')
        if not phone.startswith('09'):
            raise forms.ValidationError('شماره تلفن باید با 09 شروع شود.')
        if len(phone) != 11:
            raise forms.ValidationError('شماره تلفن باید 11 رقم باشد.')
        return phone

    def clean(self):
        cleaned_data = super().clean()
        selected_products = []

        products = Product.objects.all()
        for product in products:
            selected = cleaned_data.get(f'product_{product.id}')
            quantity = cleaned_data.get(f'quantity_{product.id}')

            if selected:
                # Ensure that a valid quantity is provided for selected products
                if not quantity or quantity < 1:
                    self.add_error(f'quantity_{product.id}', 'Please enter a valid quantity.')
                else:
                    selected_products.append((product, quantity))

        cleaned_data['selected_products'] = selected_products
        return cleaned_data


class TakePhone(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone']
