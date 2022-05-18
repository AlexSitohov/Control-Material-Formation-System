from django.urls import path

from test_bilet.views import *

urlpatterns = [
    path('', start_view, name='start'),
    path('<slug:facultet_slug>/', facultet_view, name='facultet'),
    path('<slug:facultet_slug>/<slug:specialnost_slug>', specialnost_view, name='specialnost'),
    path('<slug:facultet_slug>/<slug:specialnost_slug>/<slug:predmet_slug>', predmet_view, name='predmet'),
    path('<slug:facultet_slug>/<slug:specialnost_slug>/<slug:predmet_slug>/<slug:tema_slug>', tema_view, name='tema'),

]

