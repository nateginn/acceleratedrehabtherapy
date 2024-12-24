from django.contrib.sitemaps import GenericSitemap

from about.models import AboutPageConfig, TeamPageConfig, LocationPageConfig
from blog.models import BlogConfig, BlogPost
from contacts.models import ContactsConfig
from main.models import MainPageConfig
from services.models import Service

mainpage = {
    'queryset': MainPageConfig.objects.all(),
    'date_field': 'updated',
}

about = {
    'queryset': AboutPageConfig.objects.all(),
    'date_field': 'updated',
}

team = {
    'queryset': TeamPageConfig.objects.all(),
    'date_field': 'updated',
}

location = {
    'queryset': LocationPageConfig.objects.all(),
    'date_field': 'updated',
}

services_page = {
    'queryset': Service.objects.filter(visible=True),
    'date_field': 'updated',
}

blog = {
    'queryset': BlogConfig.objects.all(),
    'date_field': 'updated',
}

blog_post = {
    'queryset': BlogPost.objects.visible(),
    'date_field': 'updated',
}

contacts = {
    'queryset': ContactsConfig.objects.all(),
    'date_field': 'updated',
}

site_sitemaps = {
    'main': GenericSitemap(mainpage, changefreq='daily', priority=1),
    'services_page': GenericSitemap(services_page, changefreq='daily', priority=1),
    'blog': GenericSitemap(blog, changefreq='weekly', priority=0.5),
    'blog_post': GenericSitemap(blog_post, changefreq='weekly', priority=0.5),
    'team': GenericSitemap(team, changefreq='weekly', priority=0.5),
    'about': GenericSitemap(about, changefreq='weekly', priority=0.5),
    'location': GenericSitemap(location, changefreq='weekly', priority=0.5),
    'contacts': GenericSitemap(contacts, changefreq='weekly', priority=0.5),
}
