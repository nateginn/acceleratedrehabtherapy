from django.db import models
from django.shortcuts import resolve_url
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from solo.models import SingletonModel

from attachable_blocks.models import AttachableBlock
from base_page.models import BasePage
from libs.autoslug import AutoSlugField
from libs.stdimage.fields import StdImageField
from libs.storages.media_storage import MediaStorage

MIN_DIMENSIONS = (900, 500)
VARIATIONS = dict(
    normal=dict(
        size=(380, 465),
    ),
    mobile=dict(
        size=(540, 300),
    ),
    admin=dict(
        size=(150, 300),
        crop=False
    ),
)


class Service(MPTTModel, BasePage):
    slug = AutoSlugField(_('slug'), populate_from='title', unique=True)
    description_additional = models.TextField(_('description additional'), blank=True)
    
    important_in_menu = models.BooleanField(_('important in menu'), default=False)
    important_in_preview = models.BooleanField(_('important in preview'), default=False)
    
    sub_menu_title = models.CharField(_('Title'), help_text='Only for parent services', max_length=128, blank=True)
    parent = TreeForeignKey('self',
                            blank=True,
                            null=True,
                            verbose_name=_('parent service'),
                            related_name='children',
                            limit_choices_to={
                                'parent': None
                            }
                            )
    preview_img = StdImageField(_('preview image'),
                                blank=True,
                                storage=MediaStorage('services/preview'),
                                min_dimensions=MIN_DIMENSIONS,
                                variations=VARIATIONS,
                                admin_variation='admin',
                                crop_area=True,
                                aspects=('normal',),
                                )
    
    class MPTTMeta:
        order_insertion_by = ('sort_order',)
    
    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')
        ordering = ('sort_order',)
    
    def get_absolute_url(self):
        if self.parent:
            return resolve_url('services:sub_detail', parent_slug=self.parent.slug, slug=self.slug)
        else:
            return resolve_url('services:detail', slug=self.slug)
    
    def __str__(self):
        return self.title
