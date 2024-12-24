import re
from django_jinja.backend import Jinja2


class Jinja2Backend(Jinja2):
    def __init__(self, params):
        options = params.get("OPTIONS", {})

        self._exclude_regex = options.pop("exclude_regex", None)
        if self._exclude_regex:
            self._exclude_regex = re.compile(self._exclude_regex)

        super().__init__(params)

        if self._match_regex:
            self._match_regex = re.compile(self._match_regex)

    def match_template(self, template_name):
        if self._exclude_regex and self._exclude_regex.match(template_name):
            return False

        if self._match_regex and not self._match_regex.match(template_name):
            return False

        return True
