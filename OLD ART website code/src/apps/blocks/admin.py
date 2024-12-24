from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from suit.admin import SortableTabularInline

from attachable_blocks.admin import AttachableBlockAdmin
from project.admin.base import ModelAdminInlineMixin
from .models import (LocationBlock, OurTeamBlock, AppointmentBlock, ShareBlock, Advantages, WhyChooseUsBlock,
                     OurMissionBlock, FocusOnBlock, Focuses, InsurancesBlock, PartnersBlock, Partners, BlogBlock,
                     ServiceBlock, ContactBlock)


class AdvantagesInline(ModelAdminInlineMixin, SortableTabularInline):
    model = Advantages
    extra = 0
    max_num = 3
    sortable = 'sort_order'
    suit_classes = 'suit-tab suit-tab-general'


class FocusesInline(ModelAdminInlineMixin, SortableTabularInline):
    model = Focuses
    extra = 0
    max_num = 5
    sortable = 'sort_order'
    suit_classes = 'suit-tab suit-tab-general'


class PartnersInline(ModelAdminInlineMixin, SortableTabularInline):
    model = Partners
    extra = 0
    max_num = 4
    sortable = 'sort_order'
    suit_classes = 'suit-tab suit-tab-general'


@admin.register(LocationBlock)
class LocationBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'img', 'header', 'description', 'button_text',
            ),
        }),
    )


@admin.register(OurTeamBlock)
class OurTeamBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'img', 'header', 'description', 'button_text',
            ),
        }),
    )


@admin.register(InsurancesBlock)
class InsurancesBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'img', 'header', 'description', 'button_text',
            ),
        }),
    )


@admin.register(AppointmentBlock)
class AppointmentBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header', 'description', 'btn_text', 'btn_link'
            ),
        }),
    )


@admin.register(ShareBlock)
class ShareBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'like_slogan',
            ),
        }),
    )


@admin.register(WhyChooseUsBlock)
class WhyBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (_('Customization'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header',
            ),
        }),
    )
    inlines = (AdvantagesInline,)


@admin.register(FocusOnBlock)
class FocusOnBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (_('Customization'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header',
            ),
        }),
    )
    inlines = (FocusesInline,)


@admin.register(OurMissionBlock)
class OurMissionBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header', 'description', 'slider'
            ),
        }),
    )


@admin.register(PartnersBlock)
class PartnersBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (_('Customization'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header',
            ),
        }),
    )
    inlines = (PartnersInline,)


@admin.register(BlogBlock)
class BlogBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (_('Customization'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header',
            ),
        }),
    )


@admin.register(ServiceBlock)
class ServiceBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (_('Customization'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header',
            ),
        }),
    )


@admin.register(ContactBlock)
class ContactBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (_('Customization'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header', 'consultation_title', 'consultation_btn_text'
            ),
        }),
    )
