from django.conf.urls import url

from .views import (
    CreateUnidadeMedida,
    ListUnidadeMedida,
    EditUnidadeMedida,
    DeleteUnidadeMedida
)

urlpatterns = [
    url(r'^create/$', CreateUnidadeMedida.as_view(), name='create'),
    url(r'^list/$', ListUnidadeMedida.as_view(), name='list'),
    url(r'^edit/(?P<id>[0-9]+)$', EditUnidadeMedida.as_view(), name='edit'),
    url(r'^delete/(?P<id>[0-9]+)$', DeleteUnidadeMedida.as_view(), name='delete'),
]
