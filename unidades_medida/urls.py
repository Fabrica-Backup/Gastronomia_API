from django.conf.urls import url
from django.contrib import admin

from .views import CreateUnidadeMedida, ListUnidadeMedida, DetailsUnidadeMedida

urlpatterns = [
    url(r'^create/$', CreateUnidadeMedida.as_view(), name='create'),
    url(r'^list/$', ListUnidadeMedida.as_view(), name='list'),
    url(r'^details/(?P<pk>[0-9]+)$', DetailsUnidadeMedida.as_view(), name='details'),
]
