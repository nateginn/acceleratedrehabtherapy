from jinja2.nodes import Output, MarkSafeIfAutoescape, CallBlock, Keyword, ContextReference
from jinja2.ext import Extension as BaseExtension


class Extension(BaseExtension):
    """
        Базовый класс шаблонного тэга Jinja2.

        Параметры:
            tags            - множество обрабатываемых тэгов
            simple          - тэг, не имеющий завершающей пары (endtag)
            marksafe        - для simple-тэгов помечает вывод как безопасный
            takes_context   - нужно ли передавать первым параметров контекст.
    """
    tags = {}
    simple = True
    marksafe = True
    takes_context = False

    def parse(self, parser):
        tag = parser.stream.current.value
        lineno = next(parser.stream).lineno
        args, kwargs = self.parse_args(parser, lineno)

        call = self.call_method(
            '_%s' % tag,
            args,
            kwargs,
            lineno=lineno
        )

        if self.simple:
            if self.marksafe:
                call = MarkSafeIfAutoescape(call)
            return Output([call])
        else:
            body = parser.parse_statements(['name:end{}'.format(tag)], drop_needle=True)
            return CallBlock(call, [], [], body).set_lineno(lineno)

    def parse_args(self, parser, lineno):
        args = []
        kwargs = []

        if self.takes_context:
            args.insert(0, ContextReference(lineno=lineno))

        while parser.stream.current.type != 'block_end':
            if parser.stream.current.type == 'name' and parser.stream.look().type == 'assign':
                key = parser.stream.current.value
                parser.stream.skip(2)
                value = parser.parse_expression()
                kwargs.append(Keyword(key, value, lineno=value.lineno))
            else:
                if kwargs:
                    parser.fail('Invalid argument syntax for Extension tag',
                        parser.stream.current.lineno)
                args.append(parser.parse_expression())

        return args, kwargs