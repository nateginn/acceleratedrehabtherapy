from django.db import models
from django.utils.translation import ugettext_lazy as _

from attachable_blocks.models import AttachableBlock
from libs.description import description


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Testimonial(models.Model):
    name = models.CharField(_('person name'), max_length=128)
    position = models.CharField(_('person position'), max_length=128)
    star = IntegerRangeField(min_value=1, max_value=5)
    testimonial = models.TextField(_('testimonial'))
    
    visible = models.BooleanField(_('visible'), default=True)
    sort_order = models.IntegerField(_('order'), default=0)
    
    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')
        ordering = ('sort_order',)
    
    def __str__(self):
        return self.name
    
    @property
    def short_text(self):
        return description(self.testimonial, 300, 310)
    
    @property
    def is_long(self):
        return len(self.short_text) < len(self.testimonial)


class TestimonialsBlock(AttachableBlock):
    BLOCK_VIEW = 'testimonials.views.block_render'
    header = models.CharField(_('header'), max_length=128, blank=True)
    
    class Meta:
        verbose_name = _('Testimonials')
        verbose_name_plural = _('Testimonials')
