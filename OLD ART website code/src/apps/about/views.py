from django.shortcuts import resolve_url

from base_page.views import BasePageSingletonView
from .models import AboutPageConfig, LocationPageConfig, TeamPageConfig


class IndexView(BasePageSingletonView):
    model = AboutPageConfig


class LocationView(BasePageSingletonView):
    model = LocationPageConfig
    
    def get_context_data(self, **kwargs):
        self.request.breadcrumbs.add(AboutPageConfig.get_solo().title, resolve_url('about:index'))
        context = super().get_context_data(**kwargs)
        return context


class TeamView(BasePageSingletonView):
    model = TeamPageConfig
    
    def get_context_data(self, **kwargs):
        self.request.breadcrumbs.add(AboutPageConfig.get_solo().title, resolve_url('about:index'))
        context = super().get_context_data(**kwargs)
        return context
