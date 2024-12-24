from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from suit.admin import SortableModelAdmin

from attachable_blocks.admin import AttachableBlockAdmin
from libs.description import description
from project.admin import ModelAdminMixin
from .models import Testimonial, TestimonialsBlock


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdminMixin, SortableModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'star', 'name', 'position', 'testimonial',
            ),
        }),
    )
    sortable = 'sort_order'
    list_filter = ('star',)
    list_display = ('name', 'testimonial_text', 'star')
    list_editable = ('star',)
    suit_form_tabs = (
        ('general', _('General')),
    )
    
    def has_change_permission(self, request, obj=None):
        return True
    
    @staticmethod
    def testimonial_text(obj):
        return description(obj.testimonial, 50, 150)


@admin.register(TestimonialsBlock)
class TestimonialsBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (_('Customization'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header',
            ),
        }),
    )
