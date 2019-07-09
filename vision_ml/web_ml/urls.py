from django.conf.urls import url
from . import views  # add
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.first_view, name='first_view'),
    url(r'^uimage/$', views.uimage, name='uimage'),
    url(r'^obj/$', views.objectDector_html, name='obj'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)