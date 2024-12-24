from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Config(AppConfig):
    name = 'rating'
    verbose_name = _('Voting')

    def ready(self):
        from . import views_ajax
