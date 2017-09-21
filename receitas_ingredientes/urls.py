from django.conf.urls import url

from .views import (
    CreateReceitaIngrediente,
    ListReceitaIngrediente,
    EditReceitaIngrediente,
    DeleteReceitaIngrediente
)

urlpatterns = [
    url(r'^create/$', CreateReceitaIngrediente.as_view(), name='create'),
    url(r'^list/$', ListReceitaIngrediente.as_view(), name='list'),
    url(r'^edit/(?P<id>[0-9]+)$', EditReceitaIngrediente.as_view(), name='edit'),
    url(r'^delete/(?P<id>[0-9]+)$', DeleteReceitaIngrediente.as_view(), name='delete'),
]
