from django.contrib import admin
from django.conf.urls import url
from . import admin_views


app_name = 'admin_social_networks'
urlpatterns = [
    url(r'^twitter_token/$', admin.site.admin_view(admin_views.TwitterTokenView.as_view()), name='twitter_token'),
    url(r'^facebook_token/$', admin.site.admin_view(admin_views.FacebookTokenView.as_view()), name='facebook_token'),
    url(r'^instagram_token/$', admin.site.admin_view(admin_views.InstagramTokenView.as_view()), name='instagram_token'),
    url(r'^linkedin_token/$', admin.site.admin_view(admin_views.LinkedinTokenView.as_view()), name='linkedin_token'),
]
