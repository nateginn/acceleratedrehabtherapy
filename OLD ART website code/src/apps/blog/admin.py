from django.conf import settings
from django.contrib import admin
from django.utils import dateformat
from django.utils.timezone import localtime
from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin
from base_page.admin import BasePageSingletonAdmin, BasePageAdmin

from seo.admin import SeoModelAdminMixin
from social_networks.admin import AutoPostMixin
from .models import BlogConfig, BlogPost


@admin.register(BlogConfig)
class BlogConfigAdmin(BasePageSingletonAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(BasePageAdmin):
    fieldsets = (
        (_('Header block'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header', 'description', 'button_text',
            ),
        }),
        (_('Preview'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'img', 'title', 'slug', 'note', 'status', 'date',
            ),
        }),
        (_('Content'), {
            'classes': ('suit-tab', 'suit-tab-content'),
            'fields': (
                'text_top', 'text_bottom',
            ),
        }),
    )
    # inlines = B.inlines
    
    list_filter = ('status',)
    date_hierarchy = 'date'
    search_fields = ('header',)
    list_display = ('view', '__str__', 'date_fmt', 'status')
    list_display_links = ('__str__',)
    actions = ('make_public_action', 'make_draft_action')
    prepopulated_fields = {
        'slug': ('title',)
    }
    
    # suit_form_tabs = StdPageAdmin.suit_form_tabs
    
    def date_fmt(self, obj):
        return dateformat.format(localtime(obj.date), settings.DATETIME_FORMAT)
    
    date_fmt.short_description = _('Publication date')
    date_fmt.admin_order_field = 'date'
    
    def get_autopost_text(self, obj):
        return obj.description
    
    def make_public_action(self, request, queryset):
        queryset.update(status=self.model.STATUS_PUBLIC)
    
    make_public_action.short_description = _('Make public')
    
    def make_draft_action(self, request, queryset):
        queryset.update(status=self.model.STATUS_DRAFT)
    
    make_draft_action.short_description = _('Make draft')


