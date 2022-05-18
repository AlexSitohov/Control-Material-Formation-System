from django.contrib.auth.models import User
from django.db.models import (
    Model,
    SET_NULL,
    CharField,
    BooleanField,
    OneToOneField,
)


class Account(Model):
    login = OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=SET_NULL,
        verbose_name='логин',
    )
    first_name = CharField(
        'имя',
        max_length=70,
    )
    last_name = CharField(
        'фамилия',
        max_length=70,
    )
    can_create = BooleanField(
        'может создавать тесты',
        default=True,
    )
    status = CharField(
        'статус пользователя: студент/учитель',
        max_length=50
    )

    def __str__(self):
        username = f' ({self.login.username})' if self.login else ''
        return f'{self.first_name} {self.last_name} - {self.status} {username}'

    class Meta:
        db_table = 'account'
        verbose_name = 'аккаунт'
        verbose_name_plural = 'аккаунты'
