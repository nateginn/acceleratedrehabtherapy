from django.conf.urls import url
from . import views


app_name = 'users'
urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^reset/$', views.PasswordResetView.as_view(), name='reset'),
    url(r'^reset_done/$', views.ResetDoneView.as_view(), name='reset_done'),
    url(r'^reset_confirm/$', views.ResetConfirmView.as_view(), name='reset_self'),
    url(r'^reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.ResetConfirmView.as_view(), name='reset_confirm'),
    url(r'^reset_complete/$', views.ResetCompleteView.as_view(), name='reset_complete'),
    url(r'^reset_password/$', views.ResetConfirmView.as_view(), name='reset_password'),
]
