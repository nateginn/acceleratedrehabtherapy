from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin
from suit.admin import SortableModelAdmin

from attachable_blocks.admin import AttachedBlocksStackedInline
from seo.admin import SeoModelAdminMixin


class TopBlocksInline(AttachedBlocksStackedInline):
    suit_classes = 'suit-tab suit-tab-blocks'
    verbose_name = _('Block')
    verbose_name_plural = _('Page top blocks')
    set_name = 'top'


class BottomBlocksInline(AttachedBlocksStackedInline):
    suit_classes = 'suit-tab suit-tab-blocks'
    verbose_name = _('Block')
    verbose_name_plural = _('Page bottom blocks')
    set_name = 'bottom'


class BasePageMixin(SeoModelAdminMixin):
    inlines = (TopBlocksInline, BottomBlocksInline)
    suit_form_tabs = (
        ('general', _('General')),
        ('content', _('Page content')),
        ('blocks', _('Blocks')),
    )


class BasePageAdmin(BasePageMixin, SortableModelAdmin):
    fieldsets = (
        (_('Header block'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'slug', 'button_text', 'header', 'description',
            ),
        }),
        (_('Content'), {
            'classes': ('suit-tab', 'suit-tab-content'),
            'fields': (
                'text_top', 'text_bottom',
            ),
        }),
    )
    
    sortable = 'sort_order'
    prepopulated_fields = {
        'slug': ('title',)
    }


class BasePageSingletonAdmin(BasePageMixin, SingletonModelAdmin):
    fieldsets = (
        (_('Header block'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'button_text', 'header', 'description',
            ),
        }),
        (_('Content'), {
            'classes': ('suit-tab', 'suit-tab-content'),
            'fields': (
                'text_top', 'text_bottom',
            ),
        }),
    )
