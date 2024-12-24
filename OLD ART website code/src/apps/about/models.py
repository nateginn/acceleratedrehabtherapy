from django.shortcuts import resolve_url
from django.utils.translation import ugettext_lazy as _

from base_page.models import BasePageSingleton


class AboutPageConfig(BasePageSingleton):
    def get_absolute_url(self):
        return resolve_url('about:index')


class LocationPageConfig(BasePageSingleton):
    class Meta:
        verbose_name = _('location')
    
    def get_absolute_url(self):
        return resolve_url('about:location')


class TeamPageConfig(BasePageSingleton):
    class Meta:
        verbose_name = _('our team')
    
    def get_absolute_url(self):
        return resolve_url('about:team')
