from django.template import loader
from libs import jinja2
from libs.cache.cached import cached
from ..models import SocialLink


@cached()
def get_links():
    return tuple(SocialLink.objects.all())


@jinja2.extension
class SocialLinksExtension(jinja2.Extension):
    tags = {'social_links'}
    takes_context = True

    def _social_links(self, context, classes='', template='social_networks/social_links.html'):
        request = context.get('request')
        if not request:
            return ''

        links = get_links()
        if not links:
            return ''

        return loader.render_to_string(template, {
            'links': links,
            'classes': classes,
        }, request=request)
