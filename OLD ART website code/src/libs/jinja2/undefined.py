from jinja2 import Undefined
from jinja2.utils import internalcode


class UndefinedSilently(Undefined):
    @internalcode
    def __getattr__(self, name):
        if name[:2] == '__':
            raise AttributeError(name)

        new_name = '%s.%s' % (self._undefined_name, name)
        return self.__class__(name=new_name)

    def __call__(self, *args, **kwargs):
        return self

