from django import forms
from django.utils.translation import get_language


class GalleryWidget(forms.Widget):
    template_name = 'gallery/admin/widget.html'

    class Media:
        js = (
            'common/js/jquery.Jcrop.js',
            'common/js/plupload/plupload.full.min.js',
            'common/js/plupload/i18n/%s.js' % (get_language(), ),
            'common/js/cropdialog.js',
            'common/js/uploader.js',
            'gallery/admin/js/gallery_class.js',
            'gallery/admin/js/jquery.gallery.js',
            'gallery/admin/js/gallery.js',
        )
        css = {
            'all': (
                'common/css/jcrop/jquery.Jcrop.css',
                'admin/css/cropdialog/cropdialog.css',
                'gallery/admin/css/gallery.css',
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        try:
            gallery = self.queryset.model._meta.base_manager.get(pk=value)
        except self.queryset.model.DoesNotExist:
            gallery = None

        context.update({
            'name': name,
            'gallery': gallery,
            'gallery_model': self.queryset.model,
        }, **self.context)
        return context
