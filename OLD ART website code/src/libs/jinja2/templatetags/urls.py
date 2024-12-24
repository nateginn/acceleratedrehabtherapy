from jinja2.filters import contextfilter
from django.urls import reverse
from django_jinja.library import filter, global_function


@contextfilter
@filter(name='absolute_uri')
def do_absolute_uri(context, location, strict=True):
    """
    Формирование абсолютного URL из относительного.
    Параметр strict требует наличие request в контексте.

    Пример:
        <a href="{{ static('img/image.jpg')|absolute_uri(false) }}">

    :type context: dict
    :type location: str
    :type strict: bool
    :rtype: str
    """
    request = context.get('request')
    if request is None:
        if strict:
            raise RuntimeError('request undefined')
        else:
            return location
    return request.build_absolute_uri(location)


@global_function(name='url')
def do_url(view_or_model, *args, **kwargs):
    if hasattr(view_or_model, 'get_absolute_url'):
        return view_or_model.get_absolute_url()
    return reverse(view_or_model, args=args, kwargs=kwargs)
