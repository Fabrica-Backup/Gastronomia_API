from django.conf.urls import url

from .views import CreateAula, ListAula, EditAula, DeleteAula

urlpatterns = [
    url(r'^create/$', CreateAula.as_view(), name='create'),
    url(r'^list/$', ListAula.as_view(), name='list'),
    url(r'^edit/(?P<id>[0-9]+)$', EditAula.as_view(), name='edit'),
    url(r'^delete/(?P<id>[0-9]+)$', DeleteAula.as_view(), name='delete'),
]



