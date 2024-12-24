from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.defaults import bad_request, permission_denied, page_not_found, server_error
from .common import urlpatterns


urlpatterns = (
    [
        url(r'^400/$', bad_request, kwargs={'exception': None}),
        url(r'^403/$', permission_denied, kwargs={'exception': None}),
        url(r'^404/$', page_not_found, kwargs={'exception': None}),
        url(r'^500/$', server_error),
    ] +
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
    urlpatterns
)
