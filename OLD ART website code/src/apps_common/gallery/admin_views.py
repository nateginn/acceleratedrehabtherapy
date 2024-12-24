import importlib
from django.apps import apps
from django.template import loader
from django.views.generic import View
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse, Http404
from libs.upload import upload_chunked_file, TemporaryFileNotFoundError, NotLastChunk


class GalleryView(View):
    gallery_model = None
    require_gallery_model = True

    gallery = None
    require_gallery = False

    item = None
    require_item = False

    def _detect_objects(self, data):
        # Определение модели галереи
        app_label = data.get('app_label')
        model_name = data.get('model_name')
        try:
            self.gallery_model = apps.get_model(app_label, model_name)
        except LookupError:
            if self.require_gallery_model:
                return JsonResponse({
                    'success': False,
                    'message': _('Gallery model not found')
                })

        # Галерея
        try:
            gallery_id = int(data.get('gallery_id'))
        except (TypeError, ValueError):
            gallery_id = 0
            if self.require_gallery:
                return JsonResponse({
                    'success': False,
                    'message': _('Gallery not found')
                })

        try:
            self.gallery = self.gallery_model.objects.get(pk=gallery_id)
        except self.gallery_model.DoesNotExist:
            if self.require_gallery:
                return JsonResponse({
                    'success': False,
                    'message': _('Gallery not found')
                })

        # Элемент
        if self.gallery:
            try:
                item_id = int(data.get('item_id'))
            except (TypeError, ValueError):
                item_id = 0
                if self.require_item:
                    return JsonResponse({
                        'success': False,
                        'message': _('Item not found')
                    })

            try:
                self.item = self.gallery.items.model.objects.get(pk=item_id)
            except self.gallery.items.model.DoesNotExist:
                if self.require_item:
                    return JsonResponse({
                        'success': False,
                        'message': _('Item not found')
                    })

    def get(self, request):
        self._detect_objects(request.GET)

    def post(self, request):
        self._detect_objects(request.POST)


class GalleryCreate(GalleryView):
    """ Создание галереи """
    require_gallery_model = True

    def post(self, request):
        super().post(request)

        # Создание галереи
        gallery = self.gallery_model.objects.create()

        return JsonResponse({
            'success': True,
            'gallery_id': gallery.pk,
            'html': loader.render_to_string(gallery.ADMIN_TEMPLATE_ITEMS, {
                'gallery': gallery,
                'name': request.POST.get('field_name'),
            }, request=self.request)
        })


class GalleryDelete(GalleryView):
    """ Удаление галереи """
    require_gallery_model = True
    require_gallery = True

    def post(self, request):
        super().post(request)
        self.gallery.delete()
        return JsonResponse({
            'success': True,
            'html': loader.render_to_string(self.gallery.ADMIN_TEMPLATE_EMPTY,
                request=self.request
            )
        })


class UploadImage(GalleryView):
    """ Загрузка картинки """
    require_gallery_model = True
    require_gallery = True

    def post(self, request):
        super().post(request)

        try:
            uploaded_file = upload_chunked_file(request, 'image')
        except TemporaryFileNotFoundError as e:
            return JsonResponse({
                'success': False,
                'message': str(e),
            })
        except NotLastChunk:
            return JsonResponse({
                'success': True,
            })

        # Создание экземпляра элемента галереи
        item = self.gallery.IMAGE_MODEL(
            gallery=self.gallery,
        )
        item.image.save(uploaded_file.name, uploaded_file, save=False)
        uploaded_file.close()

        try:
            item.full_clean()
        except ValidationError as e:
            item.image.delete(save=False)
            return JsonResponse({
                'success': False,
                'message': '; '.join(e.messages),
            })
        else:
            item.save()

        try:
            self.gallery.clean()
        except ValidationError as e:
            item.delete()
            return JsonResponse({
                'success': False,
                'message': '; '.join(e.messages),
            })

        response = {
            'success': True,
            'id': item.pk,
            'preview_url': item.admin_variation.url,
            'show_url': item.admin_show_url,
            'source_url': item.image.url_nocache,
            'source_size': ','.join(map(str, item.image.dimensions)),
        }
        return JsonResponse(response)


class UploadVideoImage(GalleryView):
    """ Загрузка видео """
    require_gallery_model = True
    require_gallery = True

    def post(self, request):
        super().post(request)

        # Создание экземпляра элемента галереи
        item = self.gallery.VIDEO_LINK_MODEL(
            gallery=self.gallery,
            video=request.POST.get('link', '')
        )

        try:
            item.full_clean()
        except ValidationError as e:
            item.video_preview.delete(save=False)
            return JsonResponse({
                'success': False,
                'message': '; '.join(e.messages),
            })
        else:
            item.save()

        try:
            self.gallery.clean()
        except ValidationError as e:
            item.delete()
            return JsonResponse({
                'success': False,
                'message': '; '.join(e.messages),
            })

        return JsonResponse({
            'success': True,
            'id': item.pk,
            'preview_url': item.admin_variation.url,
            'show_url': item.admin_show_url,
        })


class DeleteItem(GalleryView):
    """ Удаление элемента галереи """
    require_gallery_model = True
    require_gallery = True
    require_item = True

    def post(self, request):
        super().post(request)
        self.item.delete()
        return JsonResponse({
            'success': True
        })


class RotateItem(GalleryView):
    """ Поворот картинки """
    require_gallery_model = True
    require_gallery = True
    require_item = True

    def post(self, request):
        super().post(request)

        if not self.item.is_image:
            return JsonResponse({
                'success': False,
                'message': _('Item is not image')
            })
        elif not self.item.image.exists():
            return JsonResponse({
                'success': False,
                'message': _('Image is not exists')
            })

        direction = request.GET.get('direction')
        if not direction or direction not in ('left', 'right'):
            return JsonResponse({
                'success': False,
                'message': _('Invalid rotate direction')
            })

        if direction == 'left':
            self.item.image.rotate(-90)
        else:
            self.item.image.rotate(90)

        return JsonResponse({
            'success': True,
            'preview_url': self.item.admin_variation.url_nocache,
            'source_url': self.item.image.url_nocache,
        })


class CropItem(GalleryView):
    """ Обрезка картинки """
    require_gallery_model = True
    require_gallery = True
    require_item = True

    def post(self, request):
        super().post(request)

        if not self.item.is_image:
            return JsonResponse({
                'success': False,
                'message': _('Item is not image')
            })
        elif not self.item.image.exists():
            return JsonResponse({
                'success': False,
                'message': _('Image is not exists')
            })

        try:
            croparea = request.POST.get('coords', '')
            self.item.image.recut(croparea=croparea)
        except ValueError:
            return JsonResponse({
                'success': False,
                'message': _('Invalid crop coords')
            })

        return JsonResponse({
            'success': True,
            'preview_url': self.item.admin_variation.url_nocache
        })


class EditItem(GalleryView):
    """ Получение описания """
    require_gallery_model = True
    require_gallery = True
    require_item = True

    def get(self, request):
        super().get(request)

        module_name, form_name = self.item.EDIT_FORM.rsplit('.', 1)
        try:
            forms_module = importlib.import_module(module_name)
        except ImportError:
            return JsonResponse({
                'success': False,
                'message': _('Not found form class')
            })

        FormClass = getattr(forms_module, form_name, None)
        if FormClass is None:
            return JsonResponse({
                'success': False,
                'message': _('Not found form class')
            })

        return JsonResponse({
            'success': True,
            'html': loader.render_to_string('gallery/admin/form.html', {
                'form': FormClass(instance=self.item)
            }, request=self.request)
        })

    def post(self, request):
        super().post(request)

        module_name, form_name = self.item.EDIT_FORM.rsplit('.', 1)
        try:
            forms_module = importlib.import_module(module_name)
        except ImportError:
            return JsonResponse({
                'success': False,
                'message': _('Not found form class')
            })

        FormClass = getattr(forms_module, form_name, None)
        if FormClass is None:
            return JsonResponse({
                'success': False,
                'message': _('Not found form class')
            })

        form = FormClass(request.POST, request.FILES, instance=self.item)
        if form.is_valid():
            form.save()
        else:
            return JsonResponse({
                'success': False,
                'errors': form.error_dict,
            })

        return JsonResponse({
            'success': True
        })


class SortItems(GalleryView):
    """ Установка описания """
    require_gallery_model = True
    require_gallery = True

    def post(self, request):
        super().post(request)

        try:
            item_ids = request.POST.get('item_ids', '').split(',')
            item_ids = map(int, item_ids)
        except (TypeError, ValueError):
            raise Http404

        for order, item_id in enumerate(item_ids, start=1):
            try:
                item = self.gallery.items.model.objects.get(pk=item_id)
            except self.gallery.items.model.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': _('Gallery item #%s not found' % item_id)
                })
            else:
                item.sort_order = order
                item.save()

        return JsonResponse({
            'success': True
        })
