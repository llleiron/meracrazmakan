from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls
from Grancum.views import create_user, index
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title="Ռազմական")),
    # path('Grancum/', include('Grancum.urls')),
    path('user', index),
    path('user', create_user),
    path('YndhanurTexekutyunner/', include('YndhanurTexekutyunner.urls')),
    path('Anamnez/', include('Anamnez.urls')),
    path('Tsarayutyun/', include('Tsarayutyun.urls')),
    path('Fizikakan/', include('Fizikakan.urls')),
    path('Myus/', include('Myus.urls'))
]