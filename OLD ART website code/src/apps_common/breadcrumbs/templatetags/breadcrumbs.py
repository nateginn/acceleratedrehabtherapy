from django.template import loader
from libs import jinja2


@jinja2.extension
class BreadcrumbsExtension(jinja2.Extension):
    tags = {'breadcrumbs'}
    takes_context = True

    def _breadcrumbs(self, context, template='breadcrumbs/block.html'):
        request = context.get('request')
        if not request:
            return ''

        return loader.render_to_string(template, {
            'breadcrumbs': getattr(request, 'breadcrumbs', None),
        }, request=request)
