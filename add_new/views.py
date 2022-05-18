from django.shortcuts import render, redirect

from add_new.forms import *


def add_new(request):
    return render(request, 'add_new/start.html', {'title': 'Добавить новое'})


def add_new_view_vopros(request):
    if request.method == "POST":
        form = AddNewVopros(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                form.save()
                return redirect('/')
            except:
                form.add_error(None, 'Ошибка добавления статьи')
    else:
        form = AddNewVopros
    context = {
        'title': 'Добавить новое',
        'form': form
    }
    return render(request, 'add_new/add_new_vopros.html', context=context)
