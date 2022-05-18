from django.contrib.admin import (
    ModelAdmin,
    register,
)

from account.models import Account


@register(Account)
class AccountModelAdmin(ModelAdmin):
    pass
