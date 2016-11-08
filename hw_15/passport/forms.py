from datetime import date
from django import forms
from django.core.validators import RegexValidator

DATE_INPUT_FORMATS = ['%d.%m.%Y',]

class PassportForm(forms.Form):
    series = forms.CharField(label='Серия', min_length=5, max_length=5, validators=[RegexValidator(r'^(\d{2})\ (\d{2})$', 'Введите серию в формате ЧЧ ЧЧ')])
    number = forms.CharField(label='Номер', min_length=6, max_length=6, validators=[RegexValidator(r'^(\d{6})$', 'Введите номер паспорта в формате ЧЧЧЧЧЧ')])
    issue_date = forms.DateField(label='Дата выдачи', input_formats=DATE_INPUT_FORMATS)
    subdivision_code = forms.CharField(label='Код подразделения', min_length=7, max_length=7, validators=[RegexValidator(r'^(\d{3})-(\d{3})$', 'Введите код подразделения в формате ЧЧЧ-ЧЧЧ')])
    issuer = forms.CharField(label='Кем выдан', min_length=3, max_length=256, validators=[RegexValidator(r'^[-№\d\'\.\,\’\«\»\" а-яА-ЯёЁ]+$', 'Поле кем выдан должно содержать только буквы русского языка, знаки препинания и цифры')])
    place_of_birth = forms.CharField(label='Место рождения', min_length=3, max_length=256, validators=[RegexValidator(r'^[-\'\.\,\’\«\»\" а-яА-ЯёЁ]+$', 'Место рождения должно содержать только буквы русского языка и знаки препинания')])


    def clean_issue_date(self):
        d = self.cleaned_data['issue_date']
        if d > date.today():
            raise forms.ValidationError("Дата не может быть больше текущей!")
        return d
