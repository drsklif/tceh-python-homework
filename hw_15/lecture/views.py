from django.shortcuts import render
from django.contrib import messages
from lecture.forms import OrderForm

def lecture(request):
    if request.method == 'GET':
        form = OrderForm()
    else:
        form = OrderForm(request.POST)
        storage = messages.get_messages(request)
        storage.used = True
        if form.is_valid():
            messages.success(request, 'Заказ осуществлен')
        else:
            messages.error(request, 'Ошибка валидации')

    return render(request, 'lecture/lecture.html', {'form': form})
