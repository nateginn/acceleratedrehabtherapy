import os
import re
import hashlib
from django.conf import settings
from django.core.cache import cache
from django.utils.safestring import mark_safe
from django.template import loader
from django.contrib.staticfiles.storage import staticfiles_storage
from pipeline.exceptions import PackageNotFound
from pipeline.templatetags import pipeline
from pipeline.compressors import URL_DETECTOR
from libs import jinja2

NON_REWRITABLE_URL = re.compile(r'^(#|http:|https:|data:|//|/)')


class StylesheetNode(pipeline.StylesheetNode):
    """
        Добавлено время изменения файла
    """
    def render_css(self, package, path, template_name=None):
        if not staticfiles_storage.exists(path):
            return ''

        template_name = package.template_name or template_name or "pipeline/css_default.html"
        modified = staticfiles_storage.modified_time(path).timestamp()
        context = package.extra_context
        context.update({
            'url': mark_safe(staticfiles_storage.url(path)),
            'modified': int(modified),
        })
        return loader.render_to_string(template_name, context)


class InlineStylesheetNode(pipeline.StylesheetNode):
    def expand_urls(self, path, content):
        path_prefix = os.path.dirname(path)

        def reconstruct(match):
            asset_url = match.group(2)
            if not NON_REWRITABLE_URL.match(asset_url):
                asset_url = os.path.normpath(os.path.join(settings.STATIC_URL, path_prefix, asset_url))
            return "url(%s)" % asset_url

        return re.sub(URL_DETECTOR, reconstruct, content)

    def render_css(self, package, path, template_name=None):
        cache_key = ':'.join((
            self.name,
            str(staticfiles_storage.modified_time(path).timestamp()),
        ))
        cache_key = hashlib.md5(cache_key.encode()).hexdigest()
        if cache_key not in cache:
            cache.set(
                cache_key,
                self.render_individual_css(package, [path]),
                timeout=3600
            )
        return cache.get(cache_key)

    def render_individual_css(self, package, paths, **kwargs):
        html = ''.join(
            self.expand_urls(path, open(staticfiles_storage.path(path), 'r').read())
            for path in paths
        )
        return mark_safe('<style>' + html + '</style>')


class JavascriptNode(pipeline.JavascriptNode):
    """
        Добавлено время изменения файла
    """
    def render_js(self, package, path):
        template_name = package.template_name or "pipeline/js_default.html"
        modified = staticfiles_storage.modified_time(path).timestamp()
        context = package.extra_context
        context.update({
            'url': mark_safe(staticfiles_storage.url(path)),
            'modified': int(modified),
        })
        return loader.render_to_string(template_name, context)


@jinja2.extension
class PipelineExtension(jinja2.Extension):
    tags = {'stylesheet', 'javascript', 'inline_stylesheet'}

    def _stylesheet(self, name):
        node = StylesheetNode(name)
        try:
            package = node.package_for(name, 'css')
        except PackageNotFound:
            return ''
        return node.render_compressed(package, name, 'css')

    def _javascript(self, name):
        node = JavascriptNode(name)
        try:
            package = node.package_for(name, 'js')
        except PackageNotFound:
            return ''
        return node.render_compressed(package, name, 'js')

    def _inline_stylesheet(self, name):
        node = InlineStylesheetNode(name)
        try:
            package = node.package_for(name, 'css')
        except PackageNotFound:
            return ''
        return node.render_compressed(package, name, 'css')
