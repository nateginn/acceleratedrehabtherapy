from django.db import models
from django.utils.timezone import now
from django.utils.dates import WEEKDAYS
from django.shortcuts import resolve_url
from django.utils.formats import time_format
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel

from base_page.models import BasePageSingleton
from libs.multiselect_field.fields import MultiSelectField
from attachable_blocks.models import AttachableBlock
from google_maps.fields import GoogleCoordsField


class ContactsConfig(BasePageSingleton):
    header = models.TextField(_('Header'), max_length=255)
    license = models.TextField(_('License'), max_length=255, blank=True)
    
    popup_header = models.CharField(_('header'), max_length=128)
    popup_description = models.TextField(_('description'), blank=True)
    popup_button_text = models.TextField(_('Button text'), max_length=64, blank=True)
    popup_button_link = models.TextField(_('custom button link'), blank=True)
    popup_visible = models.BooleanField(_('visible'), default=False)

    def get_absolute_url(self):
        return resolve_url('contacts:index')


class Address(models.Model):
    address = models.CharField(_('address'), max_length=255)
    city = models.CharField(_('city'), max_length=255)
    region = models.CharField(_('region'), max_length=64, blank=True)
    zip = models.CharField(_('zip'), max_length=32, blank=True)
    email = models.EmailField(_('e-mail'))
    coords = GoogleCoordsField(_('coords'), blank=True)
    
    sort_order = models.PositiveIntegerField(_('sort order'))
    updated = models.DateTimeField(_('change date'), auto_now=True)
    
    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')
        ordering = ('sort_order',)
    
    @cached_property
    def phones(self):
        return tuple(PhoneNumber.objects.filter(address_id=self.id).values_list('number', flat=True))
    
    def __str__(self):
        return ', '.join(map(str, filter(bool, (self.city, self.address))))


class PhoneNumber(models.Model):
    address = models.ForeignKey(Address, related_name='+')
    number = models.CharField(_('number'), max_length=255, blank=True)
    sort_order = models.PositiveIntegerField(_('sort order'))
    
    class Meta:
        verbose_name = _('phone')
        verbose_name_plural = _('phones')
        ordering = ('sort_order',)
    
    def __str__(self):
        return self.number


class OpeningHours(models.Model):
    WEEKDAYS_ABBR = tuple([
        _('Mon'), _('Tue'), _('Wed'), _('Thu'), _('Fri'), _('Sat'), _('Sun')
    ])
    WEEKDAYS_CHOICES = tuple(
        (key, value)
        for key, value in sorted(WEEKDAYS.items())
    )
    
    address = models.ForeignKey(Address, related_name='hours')
    weekdays = MultiSelectField(_('weekdays'), choices=WEEKDAYS_CHOICES)
    start_time = models.TimeField(_('from'), null=True)
    end_time = models.TimeField(_('to'), null=True)
    
    class Meta:
        verbose_name = _('opening hours sequence')
        verbose_name_plural = _('opening hours sequences')
        ordering = ('weekdays',)
    
    @cached_property
    def day_abbrs(self):
        days = (self.WEEKDAYS_ABBR[index] for index in sorted(self.weekdays))
        return tuple(map(str, days))
    
    @cached_property
    def day_names(self):
        days = (WEEKDAYS.get(index) for index in sorted(self.weekdays))
        return tuple(map(str, days))
    
    def time_format_am(self, param):
        return param.replace('.', '')
    
    def __str__(self):
        days = list(self.weekdays)
        days_len = len(days)
        if days_len == 1:
            return '%s - %s to %s' % (
                self.WEEKDAYS_ABBR[days[0]],
                self.time_format_am(time_format(self.start_time)),
                self.time_format_am(time_format(self.end_time)),
            )
        else:
            return '%s, %s - %s to %s' % (
                self.WEEKDAYS_ABBR[days[0]],
                self.WEEKDAYS_ABBR[days[days_len - 1]],
                self.time_format_am(time_format(self.start_time)),
                self.time_format_am(time_format(self.end_time)),
            )


class NotificationReceiver(models.Model):
    config = models.ForeignKey(ContactsConfig, related_name='receivers')
    email = models.EmailField(_('e-mail'))
    
    class Meta:
        verbose_name = _('notification receiver')
        verbose_name_plural = _('notification receivers')
    
    def __str__(self):
        return self.email


class Message(models.Model):
    name = models.CharField(_('name'), max_length=128)
    phone = models.CharField(_('phone'), max_length=32, blank=True)
    email = models.EmailField(_('e-mail'), blank=True)
    message = models.TextField(_('message'), max_length=2048)
    
    date = models.DateTimeField(_('date sent'), default=now, editable=False)
    referer = models.CharField(_('from page'), max_length=512, blank=True, editable=False)
    
    class Meta:
        default_permissions = ('delete',)
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        ordering = ('-date',)
    
    def __str__(self):
        return self.name
