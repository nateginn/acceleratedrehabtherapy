from django import forms
from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils import dateformat
from django.utils.timezone import localtime
from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin
from suit.admin import SortableModelAdmin, SortableTabularInline

from attachable_blocks.admin import AttachedBlocksStackedInline
from libs.description import description
from project.admin import ModelAdminMixin, ModelAdminInlineMixin
from seo.admin import SeoModelAdminMixin
from .models import (
    ContactsConfig, Address, PhoneNumber, OpeningHours,
    NotificationReceiver, Message
)


class ContactsConfigBlocksInline(AttachedBlocksStackedInline):
    suit_classes = 'suit-tab suit-tab-blocks'


class NotificationReceiverAdmin(ModelAdminInlineMixin, admin.TabularInline):
    model = NotificationReceiver
    extra = 0
    suit_classes = 'suit-tab suit-tab-notify'


@admin.register(ContactsConfig)
class ContactsConfigAdmin(SeoModelAdminMixin, SingletonModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'header', 'license'
            ),
        }),
        ('Popup message', {
            'classes': ('suit-tab', 'suit-tab-popup'),
            'fields': (
                'popup_header', 'popup_description', 'popup_button_text', 'popup_button_link', 'popup_visible'
            ),
        }),
    )
    inlines = (NotificationReceiverAdmin, ContactsConfigBlocksInline)
    suit_form_tabs = (
        ('general', _('General')),
        ('popup', _('Popup')),
        ('notify', _('Notifications')),
        ('blocks', _('Blocks')),
    )


class PhoneNumberAdmin(ModelAdminInlineMixin, SortableTabularInline):
    model = PhoneNumber
    extra = 0
    sortable = 'sort_order'
    suit_classes = 'suit-tab suit-tab-phones'


class OpeningHoursForms(forms.ModelForm):
    class Meta:
        model = OpeningHours
        fields = '__all__'
    
    # def clean_weekdays(self):
    #     value = tuple(sorted(self.cleaned_data['weekdays']))
    #     current = value[0]
    #     for day in value[1:]:
    #         if day != current + 1:
    #             raise ValidationError(_('the sequence must be continuous'))
    #         else:
    #             current = day
    #     return value


class OpeningHoursAdmin(ModelAdminInlineMixin, admin.StackedInline):
    model = OpeningHours
    form = OpeningHoursForms
    extra = 0
    sortable = 'sort_order'
    suit_classes = 'suit-tab suit-tab-hours'


@admin.register(Address)
class AddressAdmin(ModelAdminMixin, SortableModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'address', 'city', 'region', 'zip', 'email', 'coords',
            ),
        }),
    )
    list_display = ('city', 'address',)
    sortable = 'sort_order'
    inlines = (PhoneNumberAdmin, OpeningHoursAdmin)
    suit_form_tabs = (
        ('general', _('General')),
        ('phones', _('Phones')),
        ('hours', _('Opening hours')),
    )
    
    class Media:
        js = (
            'contacts/admin/js/coords.js',
        )


@admin.register(Message)
class MessageAdmin(ModelAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'name', 'phone', 'email',
            ),
        }),
        (_('Text'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'message',
            ),
        }),
        (_('Info'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'date_fmt', 'referer',
            ),
        }),
    )
    readonly_fields = ('name', 'phone', 'email', 'message', 'date_fmt', 'referer')
    list_display = ('__str__', 'message_fmt', 'date_fmt')
    list_display_links = ('__str__', 'message_fmt', 'date_fmt')
    suit_form_tabs = (
        ('general', _('General')),
    )
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def message_fmt(self, obj):
        return description(obj.message, 60, 80)
    
    message_fmt.short_description = _('Message')
    message_fmt.admin_order_field = 'message'
    
    def date_fmt(self, obj):
        return dateformat.format(localtime(obj.date), settings.DATETIME_FORMAT)
    
    date_fmt.short_description = _('Date')
    date_fmt.admin_order_field = 'date'
