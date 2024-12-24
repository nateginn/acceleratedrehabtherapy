from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class RatingVote(models.Model):
    ip = models.GenericIPAddressField(_('ip'), db_index=True)
    rating = models.SmallIntegerField(_('rating'), validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateTimeField(_('date'), default=now, db_index=True)

    class Meta:
        ordering = ('-date', )
        verbose_name = _('vote')
        verbose_name_plural = _('votes')

    def __str__(self):
        return '%s - %d stars' % (self.ip, self.rating)
