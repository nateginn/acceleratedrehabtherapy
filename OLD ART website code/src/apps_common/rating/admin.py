from django.contrib import admin
from project.admin import ModelAdminMixin
from .models import RatingVote


@admin.register(RatingVote)
class RatingVoteAdmin(ModelAdminMixin, admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('ip', 'rating', 'date')
    readonly_fields = (
        'ip', 'rating', 'date'
    )

    def has_add_permission(self, request):
        return False
