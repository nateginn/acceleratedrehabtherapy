from django.conf.urls import url
from . import views


app_name = 'ckeditor'
urlpatterns = [
    url(r'^download_pagefile/(?P<file_id>\d+)/$', view=views.download_pagefile, name='download_pagefile'),
]
