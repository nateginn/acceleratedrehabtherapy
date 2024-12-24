from jinja2.ext import Extension
from django.conf import settings
from django.utils import timezone
from django.utils.formats import localize
from django_jinja.library import extension


@extension
class L10NExtension(Extension):
    """
    Взято из jinja2-django-tags
    """
    def __init__(self, environment):
        super().__init__(environment)
        finalize = []
        if settings.USE_TZ:
            finalize.append(timezone.template_localtime)
        if settings.USE_L10N:
            finalize.append(localize)

        if finalize:
            fns = iter(finalize)
            if environment.finalize is None:
                new_finalize = next(fns)
            else:
                new_finalize = environment.finalize
            for f in fns:
                new_finalize = self._compose(f, new_finalize)

            environment.finalize = new_finalize

    @staticmethod
    def _compose(outer, inner):
        return lambda var: outer(inner(var))
