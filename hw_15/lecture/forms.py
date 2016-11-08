from datetime import date
from django import forms
from django.core.validators import RegexValidator

goods = [
   'socks', 'balls', 'boots',
]

DATE_INPUT_FORMATS = ['%d.%m.%Y',]

class OrderForm(forms.Form):
    quantity = forms.IntegerField(label='Количество товара', min_value=1, max_value=15)
    product_name = forms.ChoiceField(label='Название товара', choices=[('', '--Выберите товар')] + [(item, item) for item in goods])
    name = forms.CharField(label='Имя', max_length=100, validators=[RegexValidator(regex=r'^\s*(?:\S+(?:\s+|$)){2,4}$', message='Имя должно содержать от 2-х до 4-х слов!')])
    delivery_date = forms.DateField(label='Дата доставки', input_formats=DATE_INPUT_FORMATS)
    delivery_address = forms.CharField(label='Адрес доставки', min_length=10, max_length=100)


    def clean_delivery_date(self):
        dd = self.cleaned_data['delivery_date']
        if dd < date.today():
            raise forms.ValidationError("Дата должна быть больше текущей!")
        if dd.isoweekday() in (6, 7):
            raise forms.ValidationError("Доставка не может быть выполнена в выходной день!")
        return dd
