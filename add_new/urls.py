from django.urls import path

from add_new.views import *

urlpatterns = [
    path('', add_new, name='add_new'),
    path('add_new_vopros/', add_new_view_vopros, name='add_new_vopros'),

  ]
