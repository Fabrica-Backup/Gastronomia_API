from django.conf.urls import url

from .views import (
    CreateIngrediente,
    ListIngrediente,
    DetailsIngrediente
)

urlpatterns = [
    url(r'^create/$', CreateIngrediente.as_view(), name='create'),
    url(r'^list/$', ListIngrediente.as_view(), name='list'),
    url(r'^details/(?P<id>[0-9]+)$', DetailsIngrediente.as_view(), name='details'),
]
