from django.conf.urls import url
from . import views

app_name = 'contacts'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^thank-you/$', views.SuccessView.as_view(), name='success'),
]
