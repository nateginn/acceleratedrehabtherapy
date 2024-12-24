from django.db import models
from django.utils.timezone import now
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import ugettext_lazy as _, ugettext
from solo.models import SingletonModel
from libs.description import description
import os
from . import conf


class SocialConfig(SingletonModel):
    google_apikey = models.CharField(_('API Key'),
        max_length=48, blank=True, default=os.environ.get('GOOGLE_MAPS_API_KEY', '')
    )

    twitter_client_id = models.CharField(_('API Key'), max_length=48, blank=True)
    twitter_client_secret = models.CharField(_('API Secret'), max_length=64, blank=True)
    twitter_access_token = models.CharField(_('Access Token'), max_length=64, blank=True)
    twitter_access_token_secret = models.CharField(_('Access Token Secret'), max_length=64, blank=True)

    facebook_client_id = models.CharField(_('App ID'), max_length=48, blank=True)
    facebook_client_secret = models.CharField(_('App Secret'), max_length=64, blank=True)
    facebook_access_token = models.TextField(_('Access Token'), blank=True)

    linkedin_client_id = models.CharField(_('API Key'), max_length=48, blank=True)
    linkedin_client_secret = models.CharField(_('API Secret'), max_length=48, blank=True)
    linkedin_access_token = models.TextField(_('Access Token'), blank=True)

    instagram_client_id = models.CharField(_('Client ID'), max_length=48, blank=True)
    instagram_client_secret = models.CharField(_('Client Secret'), max_length=48, blank=True)
    instagram_access_token = models.CharField(_('Access Token'), max_length=64, blank=True)

    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        default_permissions = ('change',)
        verbose_name = _('Settings')

    def __str__(self):
        return ugettext('Settings')


class SocialLink(models.Model):
    provider = models.CharField(_('provider'), choices=conf.SOCIAL_LINK_CHOICES, unique=True, max_length=16)
    url = models.URLField(_('URL'))
    order = models.IntegerField(_('order'), default=0)

    class Meta:
        ordering = ('order', 'id')
        verbose_name = _('Link')
        verbose_name_plural = _('Links')

    def __str__(self):
        return self.get_provider_display()


class SocialLinks(SingletonModel):
    social_google = models.URLField(_('google plus'), max_length=255, blank=True)
    social_twitter = models.URLField(_('twitter'), max_length=255, blank=True)
    social_facebook = models.URLField(_('facebook'), max_length=255, blank=True)
    social_instagram = models.URLField(_('instagram'), max_length=255, blank=True)
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        default_permissions = ('change', )
        verbose_name = _('Links')

    def __str__(self):
        return ugettext('Links to social media')


class FeedPostQuerySet(models.QuerySet):
    def scheduled_for(self, network):
        return self.filter(
            scheduled=True,
            network=network
        )


class FeedPost(models.Model):
    network = models.CharField(_('social network'),
        choices=conf.ALL_NETWORKS,
        default=conf.NETWORK_FACEBOOK,
        max_length=32
    )

    text = models.TextField(_('text'))
    url = models.URLField(_('URL'))
    scheduled = models.BooleanField(_('sheduled to share'), default=True)

    content_type = models.ForeignKey(ContentType, null=True, blank=True, editable=False)
    object_id = models.PositiveIntegerField(null=True, blank=True, editable=False)
    entity = GenericForeignKey(for_concrete_model=False)

    created = models.DateTimeField(_('created on'), default=now, editable=False)
    posted = models.DateTimeField(_('posted on'), null=True, editable=False)
    objects = FeedPostQuerySet.as_manager()

    class Meta:
        verbose_name = _('feed post')
        verbose_name_plural = _('feeds')
        ordering = ('-scheduled', '-created', )
        index_together = (('network', 'content_type', 'object_id'), )

    def __str__(self):
        if self.entity:
            return str(self.entity)
        else:
            return description(self.text, 10, 60)
