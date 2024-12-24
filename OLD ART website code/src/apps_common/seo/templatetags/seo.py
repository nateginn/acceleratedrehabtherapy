from libs import jinja2
from libs.cache.cached import cached
from ..models import Counter


@jinja2.extension
class SeoExtension(jinja2.Extension):
    tags = {'seo_counters'}
    takes_context = True

    @cached('position')
    def _seo_counters(self, context, position):
        counters = Counter.objects.filter(position=position)
        if not counters:
            return ''

        return '\n'.join(c.content for c in counters)
