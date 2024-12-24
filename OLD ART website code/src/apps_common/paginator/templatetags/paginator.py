from django.template import loader
from libs import jinja2


@jinja2.extension
class PaginatorExtension(jinja2.Extension):
    tags = {'paginator'}
    takes_context = True

    def _paginator(self, context, paginator, template='paginator/paginator.html'):
        if not paginator.current_page.has_other_pages():
            return ''

        return loader.render_to_string(template, {
            'paginator': paginator,
            'current_page_number': paginator.current_page_number,
        }, request=context.get('request'))

