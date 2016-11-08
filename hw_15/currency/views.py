from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from currency.forms import CurrencyForm

def index(request):
    if request.method == 'GET':
        return render(request, 'currency/index.html')


def currency(request):
    from currency.utils import get_quotes
    date_to = datetime.now()
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        storage = messages.get_messages(request)
        storage.used = True
        if form.is_valid():
            date_to = datetime.combine(form.cleaned_data['date_to'], datetime.min.time())
        else:
            messages.error(request, 'Некорректная дата')
    else:
        form = CurrencyForm()

    quotes = get_quotes(date_to)
    return render(request, 'currency/currency.html', {'quotes': quotes, 'form': form})
