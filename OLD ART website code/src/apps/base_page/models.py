from django.db import models
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel

from ckeditor.fields import CKEditorUploadField


class BasePageMixin(models.Model):
    title = models.CharField(_('Title'), max_length=128, help_text='for seo, preview and breadcrumbs')
    header = models.TextField(_('Header'), max_length=255)
    description = models.TextField(_('Description'), blank=True)
    button_text = models.TextField(_('Button text'), max_length=64, blank=True)
    
    text_top = CKEditorUploadField(_('Content top'), blank=True)
    text_bottom = CKEditorUploadField(_('Content bottom'), blank=True)
    
    updated = models.DateTimeField(_('change date'), auto_now=True)
    
    class Meta:
        abstract = True
        default_permissions = ('change',)
        verbose_name = _('settings')
    
    def __str__(self):
        return self.header if self.header is not None else ''


class BasePage(BasePageMixin, models.Model):
    slug = models.SlugField(_('slug'), max_length=128)
    visible = models.BooleanField(_('visible'), default=True)
    sort_order = models.PositiveIntegerField(_('order'), default=0)
    
    class Meta(BasePageMixin.Meta):
        abstract = True


class BasePageSingleton(BasePageMixin, SingletonModel):
    class Meta(BasePageMixin.Meta):
        abstract = True
