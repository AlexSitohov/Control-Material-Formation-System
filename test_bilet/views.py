from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
import random

from test_bilet.forms import ViborVoprosov
from test_bilet.models import (
    Facultet,
    Specialnost,
    Predmet,
    Tema,
    Vopros,
)


def start_view(request):
    facultets = Facultet.objects.annotate(
        count=Count('id')
    ).filter(
        count__gte=1
    ).order_by('npp')

    context = {
        'title': 'Выбор Факультета',
        'facultets': facultets,
    }

    return render(request, 'test_bilet/start.html', context=context)


def facultet_view(request, facultet_slug):
    facultet = get_object_or_404(Facultet, slug=facultet_slug)
    sprecialnosti = Specialnost.objects.filter(
        facultet=facultet,
    ).order_by('npp')

    context = {
        'title': 'Выбор Специальности',
        'facultet': facultet,
        'sprecialnosti': sprecialnosti,
    }
    return render(request, 'test_bilet/facultet.html', context=context)


def specialnost_view(request, facultet_slug, specialnost_slug):
    facultet = get_object_or_404(Facultet, slug=facultet_slug)
    specialnost = get_object_or_404(Specialnost, slug=specialnost_slug)
    predemti = Predmet.objects.filter(
        specialnost=specialnost,
    ).order_by('npp')

    context = {
        'title': 'Выбор Предмета',
        'facultet': facultet,
        'specialnost': specialnost,
        'predemti': predemti,
    }
    return render(request, 'test_bilet/specialnost.html', context=context)


def predmet_view(request, facultet_slug, specialnost_slug, predmet_slug):
    facultet = get_object_or_404(Facultet, slug=facultet_slug)
    specialnost = get_object_or_404(Specialnost, slug=specialnost_slug)
    predmet = get_object_or_404(Predmet, slug=predmet_slug)
    tems = Tema.objects.filter(
        predmet=predmet,
    ).order_by('npp')

    context = {
        'specialnost': specialnost,
        'facultet': facultet,
        'title': 'Выбор Темы',
        'predmet': predmet,
        'tems': tems,
    }
    return render(request, 'test_bilet/predmets.html', context=context)


def tema_view(request, facultet_slug, specialnost_slug, predmet_slug, tema_slug):
    specialnost = get_object_or_404(Specialnost, slug=specialnost_slug)
    facultet = get_object_or_404(Facultet, slug=facultet_slug)
    predmet = get_object_or_404(Predmet, slug=predmet_slug)
    tema = get_object_or_404(Tema, slug=tema_slug)
    first_lvl_count = 0
    second_lvl_count = 0
    third_lvl_count = 0
    first_lvl = []
    second_lvl = []
    third_lvl = []
    some_list = []
    some_list_2 = []
    some_list_3 = []
    count_vopros = 0
    some_list_4 = []
    parent_list = []

    test_count = 0
    i = 1
    ii = 1
    if request.method == "POST":
        form = ViborVoprosov(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            for v in form.cleaned_data.values():
                some_list.append(v)
            # print(some_list)
            first_lvl_count = some_list[1]
            second_lvl_count = some_list[2]
            third_lvl_count = some_list[3]
            test_count = some_list[0]
            count_vopros = first_lvl_count + second_lvl_count + third_lvl_count
            # print(count_vopros, 'fdsfs')
            while count_vopros != 0:
                some_list_4.append(i)
                i += 1
                count_vopros -= 1
            # print(first_lvl_count, second_lvl_count, third_lvl_count)
            while test_count != 0:
                some_list_3.append(ii)
                ii += 1
                test_count -= 1
            # print(some_list_3)
            voprosi = Vopros.objects.filter(
                tema=tema,

            )

            data_question = {}

            for i in range(1, some_list[0]+1):
                first_lvl_count = some_list[1]
                second_lvl_count = some_list[2]
                third_lvl_count = some_list[3]
                dict_1 = {}
                t = []
                some_list_2 = []
                t = random.sample(list(voprosi), k=len(voprosi))
                for vopros in t:
                    if vopros.level == 1:
                        if first_lvl_count > 0:
                            first_lvl.append(vopros)
                            some_list_2.append(vopros)

                        first_lvl_count -= 1
                    elif vopros.level == 2:
                        if second_lvl_count > 0:
                            second_lvl.append(vopros)
                            some_list_2.append(vopros)

                        second_lvl_count -= 1
                    else:
                        if third_lvl_count > 0:
                            third_lvl.append(vopros)
                            some_list_2.append(vopros)

                        third_lvl_count -= 1

                        # print(some_list_2)
                # for x in range(count_vopros):
                #     aa = {x: i for i in some_list_2}
                #     print(aa,'1233333333333333333333')
                dict_1 = {x: y for x, y in zip(some_list_4, some_list_2)}
                data_question[i] = dict_1

            print(data_question)
            # parent_list.append(dict_1)
            # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
            context = {
                'title': f' Билеты по теме: {tema.name}',
                'tema': tema,
                'form': form,
                'first_lvl': first_lvl,
                'second_lvl': second_lvl,
                'third_lvl': third_lvl,
                'facultet': facultet,
                'predmet': predmet,
                'specialnost': specialnost,
                'some_list_2': some_list_2,
                'test_count': test_count,
                'some_list_3': some_list_3,
                'some_list_4': some_list_4,
                'dict_1': dict_1,
                'parent_list': parent_list,
                'data_question': data_question,
            }
            # return redirect(tema.get_absolute_url())
            return render(request, 'test_bilet/test.html', context=context)

    else:
        form = ViborVoprosov
    context = {
        'title': f'Генерация билетов по теме: {tema.name}',
        'tema': tema,
        'form': form,
        'first_lvl': first_lvl,
        'second_lvl': second_lvl,
        'third_lvl': third_lvl,
        'facultet': facultet,
        'predmet': predmet,
        'specialnost': specialnost,
        'some_list_2': some_list_2,
        'test_count': test_count,
        'some_list_3': some_list_3,
    }

    return render(request, 'test_bilet/tems.html', context=context)
