from django.conf.urls import url

from . import views

app_name = 'about'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^location/$', views.LocationView.as_view(), name='location'),
    url(r'^our-team/$', views.TeamView.as_view(), name='team'),
]
