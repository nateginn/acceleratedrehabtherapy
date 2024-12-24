import re
from html import unescape
from bs4 import BeautifulSoup as Soup, NavigableString
from softhyphen.html import get_hyphenator_for_language, SOFT_HYPHEN
from django.core.cache import caches
from django.utils.html import strip_tags
from django.template import defaultfilters
from django.utils.translation import get_language
from libs import jinja2
from libs.description import description as description_func

re_nbsp = re.compile('(?<![\w’\'"])([\w’]{1,3})\s+')
re_clean_newlines = re.compile('[ \r\t\xa0]*\n')
re_many_newlines = re.compile('\n{2,}')
re_not_numbers = re.compile('[^+\d]+')


def filter_tag(tag, valid_tags=()):
    if isinstance(tag, NavigableString):
        return tag

    if tag.name in valid_tags:
        for subtag in tag.contents:
            subtag.replaceWith(filter_tag(subtag, valid_tags))
        return tag
    else:
        result = ""
        for subtag in tag.contents:
            result += str(filter_tag(subtag, valid_tags))
        return result


@jinja2.evalcontextfilter
@jinja2.filter
def striptags_except(eval_ctx, html, *args):
    """
        Удаление HTML-тэгов, кроме перечисленных в аргументе.

        Пример:
            {{ text|striptags_except:"a, p" }}
    """
    valid_tags = [item.strip() for item in args]

    soup = Soup(html, 'html5lib')
    for tag in soup.body:
        tag.replaceWith(filter_tag(tag, valid_tags))

    result = soup.body.decode_contents()
    result = re_clean_newlines.sub('\n', result).replace('\xa0', '&nbsp;')

    if eval_ctx.autoescape:
        result = jinja2.Markup(result)
    return result


def _typograf_replace(text):
    last_pos = -1
    length = 1

    def sub_func(match):
        nonlocal last_pos, length
        value = match.group(1)

        if last_pos == match.start():
            length += 1
        else:
            length = 1

        if length == 2:
            return '%s ' % value

        last_pos = match.end()
        return '%s&nbsp;' % value

    return re_nbsp.sub(sub_func, text)


@jinja2.evalcontextfilter
@jinja2.filter
def typograf(eval_ctx, html):
    """
        Удаление висячих предлогов
    """
    soup = Soup(html, 'html5lib')
    for tag in soup.findAll(text=True):
        if re_nbsp.search(tag):
            new_tag = soup.new_string(unescape(_typograf_replace(tag)))
            tag.replace_with(new_tag)

    result = soup.body.decode_contents().replace('\xa0', '&nbsp;')
    if eval_ctx.autoescape:
        result = jinja2.Markup(result)
    return result


@jinja2.evalcontextfilter
@jinja2.filter
def linewraps(eval_ctx, text, tagname='p'):
    """
        Разбивка текста на строки и оборачивание строк тэгом tagname.
        Пустые строки удаляются.
    """
    text = re_clean_newlines.sub('\n', text)
    text = re_many_newlines.sub('\n', text)
    text_lines = text.strip().split('\n')

    if eval_ctx.autoescape:
        text_lines = map(jinja2.escape, text_lines)

    result = '</{0}><{0}>'.format(tagname).join(text_lines)
    result = '<{0}>{1}</{0}>'.format(tagname, result)
    if eval_ctx.autoescape:
        result = jinja2.Markup(result)
    return result


@jinja2.evalcontextfilter
@jinja2.filter
def clean(eval_ctx, html):
    """
        Алиас для трех фильтров: striptags, linebreaksbr, typograf
    """
    result = strip_tags(str(html))
    result = defaultfilters.linebreaksbr(result)
    result = typograf(eval_ctx, result)
    return result


def get_hybernator():
    lang = get_language()
    if lang == 'ru':
        lang = 'ru-RU'

    hybernator = get_hyphenator_for_language(lang)
    hybernator.left = 4
    hybernator.right = 3
    return hybernator


def hybernate_string(string):
    hybernator = get_hybernator()
    result = (
        hybernator.inserted(word, SOFT_HYPHEN)
        for word in string.split()
    )
    return ' '.join(result)


@jinja2.evalcontextfilter
@jinja2.filter
def softhyphen(eval_ctx, html):
    """
        Вставка невидимых переносов в слова
    """
    cache = caches['default']
    key = ':'.join(map(str, (html, get_language())))
    if key in cache:
        return cache.get(key)

    soup = Soup(html, 'html5lib')
    for tag in soup.findAll(text=True):
        text = str(tag)
        if text:
            text = soup.new_string(unescape(hybernate_string(text)))
            tag.replaceWith(text)

    result = soup.body.decode_contents().replace('\xa0', '&nbsp;')
    cache.set(key, result, timeout=6 * 3600)

    if eval_ctx.autoescape:
        result = jinja2.Markup(result)
    return result


@jinja2.evalcontextfilter
@jinja2.filter
def description(eval_ctx, text, minlen, maxlen):
    result = description_func(text, minlen, maxlen)
    if eval_ctx.autoescape:
        result = jinja2.Markup(result)
    return result


@jinja2.filter
def phone(text):
    return re_not_numbers.sub('', text)


@jinja2.filter
def unescape_html(html):
    return unescape(html)
