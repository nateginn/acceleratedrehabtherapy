from django.conf.urls import url
from . import views


app_name = 'sphinx'
urlpatterns = [
    url(r'^index/(?P<index_name>\w+)/(?P<secret>\w+)/$', views.IndexPipeView.as_view(), name='index'),
]
