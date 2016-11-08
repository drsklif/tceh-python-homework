from datetime import date, datetime
from django import forms

DATE_INPUT_FORMATS = ['%d.%m.%Y',]

class CurrencyForm(forms.Form):
    date_to = forms.DateField(label='Дата', input_formats=DATE_INPUT_FORMATS, initial=date.today().strftime('%d.%m.%Y'))


    def clean_date_to(self):
        d = self.cleaned_data['date_to']
        if datetime.combine(d, datetime.min.time()) > datetime.now():
            raise forms.ValidationError("Дата не должна быть больше текущей!")
        return d
