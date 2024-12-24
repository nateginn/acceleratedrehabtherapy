from django.db import models
from django.shortcuts import resolve_url
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel

from base_page.models import BasePageSingleton
from ckeditor.fields import CKEditorUploadField
from libs.stdimage.fields import StdImageField
from libs.storages.media_storage import MediaStorage


class MainPageConfig(SingletonModel):
    title = models.CharField(_('Title'), max_length=128, blank=True, help_text='for seo, preview and breadcrumbs')
    description = models.TextField(_('Description'), blank=True)
    button_text = models.TextField(_('Button text'), max_length=64, blank=True)
    text = CKEditorUploadField(_('Content'), blank=True)
    updated = models.DateTimeField(_('change date'), auto_now=True)
    background = StdImageField(_('Background'),
                               blank=True,
                               admin_variation='admin',
                               storage=MediaStorage('main/background'),
                               crop_area=True,
                               aspects='normal',
                               min_dimensions=(1400, 800),
                               variations=dict(
                                   normal=dict(
                                       size=(1400, 800),
                                       crop=True,
                                   ),
                                   tablet=dict(
                                       size=(260, 193),
                                       crop=True,
                                   ),
                                   mobile=dict(
                                       size=(280, 207),
                                       crop=True,
                                   ),
                                   admin=dict(
                                       size=(300, 150),
                                       crop=True
                                   ),
                               ),
                               )
    
    class Meta:
        default_permissions = ('change',)
        verbose_name = _('settings')
    
    def get_absolute_url(self):
        return resolve_url('main:index')
    
    def __str__(self):
        return ugettext('Home page')
