from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Config(AppConfig):
    name = 'attachable_blocks'
    verbose_name = _('Attachable blocks')

    def ready(self):
        from django.core.cache import cache
        from . import views_ajax

        cache.delete('attachable_block_types')
