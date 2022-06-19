from django.contrib import admin
from django.contrib.admin import (
    ModelAdmin,
    register, TabularInline,
)

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from test_bilet.models import Facultet, Specialnost, Predmet, Tema, Otvet, Vopros

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ExportActionMixin


@register(Facultet)
class FacultetModelAdmin(SortableAdminMixin, ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


@register(Specialnost)
class SpecialnostModelAdmin(SortableAdminMixin, ModelAdmin):
    list_filter = ('facultet',)
    prepopulated_fields = {
        'slug': ('name',)
    }


@register(Predmet)
class PredmetModelAdmin(SortableAdminMixin, ModelAdmin):
    list_filter = ('specialnost', 'kurs', 'semestr')
    prepopulated_fields = {
        'slug': ('name',)
    }


@register(Tema)
class TemaModelAdmin(SortableAdminMixin, ModelAdmin):
    search_fields = ('name',)
    list_filter = ('predmet',)
    prepopulated_fields = {
        'slug': ('name',)
    }


class OtvetTabularInline(TabularInline):
    model = Otvet
    min_num = 2
    extra = 0


class VoprosResource(resources.ModelResource):
    tema = Field(column_name='tema',
                 attribute='tema',
                 widget=ForeignKeyWidget(Tema, 'name'))

    class Meta:
        model = Vopros
        fields = ('id', 'tema', 'full_text', 'level', 'ball')

    def tema_field(self, obj):
        return str(obj.tema.name)


@register(Vopros)
class VoprosModelAdmin(ImportExportActionModelAdmin):
    list_display = ('tema', 'full_text', 'level', 'ball')
    resource_class = VoprosResource
    search_fields = ('full_text',)
    list_filter = ('tema', 'level',)

    class VoprosModelAdmin(ModelAdmin):
        inlines = (
            OtvetTabularInline,
        )

    admin.site.site_title = 'Формирование билетов'
    admin.site.site_header = 'Администрирование сайта'

# @register(Vopros)
# class VoprosModelAdmin(ModelAdmin):
#     inlines = (
#         OtvetTabularInline,
#     )
#
#
# admin.site.site_title = 'Формирование билетов'
# admin.site.site_header = 'Администрирование сайта'
