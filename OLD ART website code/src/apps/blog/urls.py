from django.conf.urls import url
from libs.autoslug import ALIAS_REGEXP
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>{0})/$'.format(ALIAS_REGEXP), views.BlogDetailView.as_view(), name='detail'),
]
