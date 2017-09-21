from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/unidadesmedida/', include('unidades_medida.urls')),
    url(r'^api/ingredientes/', include('ingredientes.urls')),
    url(r'^api/classificacoes/', include('classificacoes.urls')),
    url(r'^api/receitasingredientes/', include('receitas_ingredientes.urls'))
]
