from django.contrib import admin
from django.conf.urls import include, url
from django.views.i18n import JavaScriptCatalog
from django.contrib.sitemaps.views import sitemap
from project.sitemaps import site_sitemaps

urlpatterns = [
    url(r'^admin/', include('admin_honeypot.urls')),
    url(r'^dladmin/social/', include('social_networks.admin_urls')),
    url(r'^dladmin/autocomplete/', include('libs.autocomplete.urls')),
    url(r'^dladmin/ckeditor/', include('ckeditor.admin_urls')),
    url(r'^dladmin/gallery/', include('gallery.admin_urls')),
    url(r'^dladmin/users/', include('users.admin_urls')),
    url(r'^dladmin/ctr/', include('admin_ctr.urls')),
    url(r'^dladmin/', include(admin.site.urls)),
    
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='jsi18n'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': site_sitemaps}),
    
    url(r'^ajax/', include('ajax_views.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    
    url(r'', include('main.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^contact/', include('contacts.urls')),
    url(r'', include('services.urls')),
]
