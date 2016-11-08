from django.shortcuts import render
from django.contrib import messages
from passport.forms import PassportForm

def passport(request):
    if request.method == 'GET':
        form = PassportForm()
    else:
        form = PassportForm(request.POST)
        storage = messages.get_messages(request)
        storage.used = True
        if form.is_valid():
            messages.success(request, 'Проверка пройдена')
        else:
            messages.error(request, 'Проверка не пройдена')

    return render(request, 'passport/passport.html', {'form': form})
