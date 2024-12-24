from django.db import models
from django.core.cache import cache
from django.db.models.functions import Coalesce
from django_jinja.library import global_function
from .. import conf
from ..models import RatingVote


@global_function
def get_rating():
    if conf.CACHE_KEY in cache:
        return cache.get(conf.CACHE_KEY)
    else:
        stats = {
            'count': RatingVote.objects.count(),
            'value': '{:.2f}'.format(RatingVote.objects.aggregate(
                rating=Coalesce(models.Avg('rating'), 0)
            )['rating'])
        }
        cache.set(conf.CACHE_KEY, stats, conf.CACHE_TIMEOUT)
        return stats
