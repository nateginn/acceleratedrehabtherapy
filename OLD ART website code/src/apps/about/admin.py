from django.contrib import admin

from base_page.admin import BasePageSingletonAdmin
from .models import AboutPageConfig, LocationPageConfig, TeamPageConfig


@admin.register(AboutPageConfig)
class AboutPageConfigAdmin(BasePageSingletonAdmin):
    pass


@admin.register(LocationPageConfig)
class LocationPageConfigAdmin(BasePageSingletonAdmin):
    pass


@admin.register(TeamPageConfig)
class TeamPageConfigAdmin(BasePageSingletonAdmin):
    pass
