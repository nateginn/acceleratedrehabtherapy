from django.conf.urls import url
from libs.autoslug import ALIAS_REGEXP
from . import views

app_name = 'services'
urlpatterns = [
    url(r'^(?P<slug>{})/$'.format(ALIAS_REGEXP), views.DetailView.as_view(), name='detail'),
    url(r'^(?P<parent_slug>{0})/(?P<slug>{0})/$'.format(ALIAS_REGEXP), views.DetailView.as_view(), name='sub_detail'),
]
