from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/un/', include('unidades_medida.urls')),
    url(r'^api/ing/', include('ingredientes.urls'))
]
