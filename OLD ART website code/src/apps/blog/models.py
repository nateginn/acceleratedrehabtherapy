from django.db import models
from django.shortcuts import resolve_url
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from base_page.models import BasePageSingleton, BasePage
from libs.stdimage.fields import StdImageField
from libs.storages.media_storage import MediaStorage


class BlogConfig(BasePageSingleton):
    def get_absolute_url(self):
        return resolve_url('blog:index')


class BlogPostQuerySet(models.QuerySet):
    def visible(self):
        return self.filter(
            status=BlogPost.STATUS_PUBLIC,
            date__lte=now()
        )


class BlogPost(BasePage):
    STATUS_DRAFT = 1
    STATUS_PUBLIC = 2
    STATUS_CHOICES = (
        (STATUS_DRAFT, _('Draft')),
        (STATUS_PUBLIC, _('Public')),
    )
    note = models.TextField(_('note'), blank=True, max_length=256)
    date = models.DateTimeField(_('publication date'), default=now)
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_DRAFT)
    img = StdImageField(_('img '),
                        storage=MediaStorage('std_page/img'),
                        min_dimensions=(380, 235),
                        admin_variation='admin',
                        crop_area=True,
                        null=True,
                        blank=True,
                        variations=dict(
                            normal=dict(
                                size=(380, 235),
                                crop=True
                            ),
                            admin=dict(
                                size=(270, 200),
                                crop=True
                            ),
                        ),
                        )
    objects = BlogPostQuerySet.as_manager()
    
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-date', '-id')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return resolve_url('blog:detail', slug=self.slug)
