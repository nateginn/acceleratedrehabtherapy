from django.conf.urls import url
from . import admin_views


app_name = 'admin_users'
urlpatterns = [
    url(r'^login_as/(?P<user_id>\d+)/$', admin_views.login_as, name='login_as'),
]
