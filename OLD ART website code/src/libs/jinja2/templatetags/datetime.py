from datetime import datetime
from django.conf import settings
from django.utils import timezone, formats
from django_jinja.library import global_function


@global_function(name='now')
def do_now(format_string=None):
    tzinfo = timezone.get_current_timezone() if settings.USE_TZ else None
    return formats.date_format(datetime.now(tz=tzinfo), format_string)
