import uuid

from django.db.models import (
    Model,
    PROTECT,
    CASCADE,
    CharField,
    TextField,
    IntegerField,
    SlugField,
    ForeignKey,
    BooleanField,
    PositiveSmallIntegerField, UUIDField,
)
from django.urls import reverse


class Facultet(Model):
    name = CharField(
        'название факультета',
        max_length=50
    )

    slug = SlugField(
        'URL',
        unique=True,
    )
    npp = PositiveSmallIntegerField(
        'сортировка',
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'facultet'
        verbose_name = 'факультет'
        verbose_name_plural = 'факультеты'
        ordering = (
            'npp',
        )

    def get_absolute_url(self):
        return reverse(
            'facultet',
            kwargs={
                'facultet_slug': self.slug,
            }
        )


class Specialnost(Model):
    name = CharField(
        'название специальности',
        max_length=50
    )

    facultet = ForeignKey(
        Facultet,
        on_delete=PROTECT,
        verbose_name='факультет'
    )

    slug = SlugField(
        'URL',
        unique=True,
    )
    npp = PositiveSmallIntegerField(
        'сортировка',
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'specialnost'
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'
        ordering = (
            'npp',
        )

    def get_absolute_url(self):
        return reverse(
            'specialnost',
            kwargs={
                'facultet_slug': self.facultet.slug,
                'specialnost_slug': self.slug
            }
        )


class Predmet(Model):
    name = CharField(
        'название предмета',
        max_length=50
    )
    specialnost = ForeignKey(
        Specialnost,
        on_delete=PROTECT,
        verbose_name='специальность'
    )
    kurs = IntegerField(
        'номер курса'
    )
    semestr = IntegerField(
        'номер семестра'
    )
    slug = SlugField(
        'URL',
        unique=True,
    )
    npp = PositiveSmallIntegerField(
        'сортировка',
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'predmet'
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'
        ordering = (
            'npp',
        )

    def get_absolute_url(self):
        return reverse(
            'predmet',
            kwargs={
                'facultet_slug': self.specialnost.facultet.slug,
                'specialnost_slug': self.specialnost.slug,
                'predmet_slug': self.slug,
            }
        )


class Tema(Model):
    name = CharField(
        'название темы',
        max_length=50
    )
    predmet = ForeignKey(
        Predmet,
        on_delete=PROTECT,
        verbose_name='предмет'
    )
    slug = SlugField(
        'URL',
        unique=True,
    )
    npp = PositiveSmallIntegerField(
        'сортировка',
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tema'
        verbose_name = 'тема'
        verbose_name_plural = 'темы'
        ordering = (
            'npp',
        )

    def get_absolute_url(self):
        return reverse(
            'tema',
            kwargs={
                'facultet_slug': self.predmet.specialnost.facultet.slug,
                'specialnost_slug': self.predmet.specialnost.slug,
                'predmet_slug': self.predmet.slug,
                'tema_slug': self.slug,

            }
        )


class Vopros(Model):
    tema = ForeignKey(
        Tema,
        on_delete=CASCADE,
        verbose_name='тема'
    )
    full_text = TextField(
        'описание вопроса',
        blank=True,
    )
    level = IntegerField(
        'сложность вопроса',
        default=1,
    )

    ball = IntegerField(
        'количество баллов',
        default=1,
    )

    def __str__(self):
        return self.full_text[:50]

    def __repr__(self):
        return self.full_text

    class Meta:
        db_table = 'vopros'
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


class Otvet(Model):
    otvet = CharField(
        'ответ',
        max_length=150,
        blank=True,
    )
    is_correct = BooleanField(
        'правильный ответ',
        default=False,
    )

    vopros = ForeignKey(
        Vopros,
        on_delete=CASCADE,
        verbose_name='вопрос',
    )

    def __str__(self):
        return self.otvet

    class Meta:
        db_table = 'otvet'
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'
