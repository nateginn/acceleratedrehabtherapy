from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from base_page.admin import BasePageAdmin
from libs.mptt import *
from .models import Service


@admin.register(Service)
class ServiceAdmin(BasePageAdmin, SortableMPTTModelAdmin):
    fieldsets = (
        ('Page config', {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'slug', 'header', 'description',
                'button_text', 'description_additional', 'parent',
                'important_in_menu', 'important_in_preview', 'visible',
                'preview_img',
            ),
        }),
        ('Sub service menu', {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'sub_menu_title',
            ),
        }),
        (_('Content'), {
            'classes': ('suit-tab', 'suit-tab-content'),
            'fields': (
                'text_top', 'text_bottom',
            ),
        }),
    )
    actions = ('make_visible', 'make_hidden')
    sortable = 'sort_order'
    prepopulated_fields = {
        'slug': ('title',),
    }
    mptt_level_indent = 20
    mptt_indent_field = '__str__'
    
    list_filter = ('visible',)
    list_display = ('__str__', 'important_in_menu', 'important_in_preview', 'visible',)
    search_fields = ('title', 'description')
    
    def make_visible(self, request, queryset):
        queryset.update(visible=True)
    
    make_visible.short_description = _('Make visible')
    
    def make_hidden(self, request, queryset):
        queryset.update(visible=False)
    
    make_hidden.short_description = _('Make hidden')
