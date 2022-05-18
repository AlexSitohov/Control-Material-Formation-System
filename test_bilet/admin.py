from django.contrib import admin
from django.contrib.admin import (
    ModelAdmin,
    register, TabularInline,
)

from adminsortable2.admin import SortableAdminMixin

from test_bilet.models import Facultet, Specialnost, Predmet, Tema, Otvet, Vopros


@register(Facultet)
class FacultetModelAdmin(SortableAdminMixin, ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


@register(Specialnost)
class SpecialnostModelAdmin(SortableAdminMixin, ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


@register(Predmet)
class PredmetModelAdmin(SortableAdminMixin, ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


@register(Tema)
class TemaModelAdmin(SortableAdminMixin, ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


class OtvetTabularInline(TabularInline):
    model = Otvet
    min_num = 2
    extra = 0


@register(Vopros)
class VoprosModelAdmin(ModelAdmin):
    inlines = (
        OtvetTabularInline,
    )


admin.site.site_title = 'Формирование билетов'
admin.site.site_header = 'Администрирование сайта'
