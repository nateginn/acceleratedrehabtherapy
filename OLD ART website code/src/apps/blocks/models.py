from django.db import models
from django.utils.translation import ugettext_lazy as _

from attachable_blocks.models import AttachableBlock
from gallery.fields import GalleryField
from gallery.models import GalleryImageItem, GalleryBase
from libs.sprite_image.fields import SpriteImageField
from libs.stdimage.fields import StdImageField
from libs.storages.media_storage import MediaStorage
from libs.file_field.fields import ImageField

MIN_DIMENSIONS = (580, 324)
VARIATIONS = dict(
    normal=dict(
        size=(580, 324),
    ),
    mobile=dict(
        size=(295, 200),
    ),
    admin=dict(
        size=(300, 150),
        crop=False
    ),
)

MIN_DIMENSIONS_ADDITIONAL = (250, 175)
VARIATIONS_ADDITIONAL = dict(
    normal=dict(
        size=(250, 175),
    ),
    mobile=dict(
        size=(125, 100),
    ),
    admin=dict(
        size=(300, 150),
        crop=False
    ),
)

MIN_DIMENSIONS_SLIDER = (770, 430)
VARIATIONS_SLIDER = dict(
    desktop=dict(
        size=(770, 430),
    ),
    mobile=dict(
        size=(385, 215),
    ),
    admin=dict(
        size=(160, 120),
    ),
)

MIN_DIMENSIONS_INSURANCES = (646, 545)
VARIATIONS_INSURANCES = dict(
    normal=dict(
        size=(646, 550),
    ),
    mobile=dict(
        size=(325, 275),
    ),
    admin=dict(
        size=(300, 150),
        crop=False
    ),
)


class LocationBlock(AttachableBlock):
    BLOCK_VIEW = 'blocks.views.location_block_render'
    
    header = models.CharField(_('header'), max_length=128, blank=True)
    description = models.TextField(_('description'), blank=True)
    button_text = models.TextField(_('Button text'), max_length=64, blank=True)
    img = StdImageField(_('image'),
                        blank=True,
                        storage=MediaStorage('blocks/location/img'),
                        admin_variation='admin',
                        min_dimensions=MIN_DIMENSIONS,
                        variations=VARIATIONS,
                        aspects='normal',
                        crop_area=True,
                        )
    
    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')


class OurTeamBlock(AttachableBlock):
    BLOCK_VIEW = 'blocks.views.our_team_block_render'
    
    header = models.CharField(_('header'), max_length=128, blank=True)
    description = models.TextField(_('description'), blank=True)
    button_text = models.TextField(_('Button text'), max_length=64, blank=True)
    img = StdImageField(_('image'),
                        blank=True,
                        storage=MediaStorage('blocks/our_team/img'),
                        admin_variation='admin',
                        min_dimensions=MIN_DIMENSIONS,
                        variations=VARIATIONS,
                        aspects='normal',
                        crop_area=True,
                        )
    
    class Meta:
        verbose_name = _('Our Team')
        verbose_name_plural = _('Our Team')


class InsurancesBlock(AttachableBlock):
    BLOCK_VIEW = 'blocks.views.insurances_block_render'
    
    header = models.CharField(_('header'), max_length=128, blank=True)
    description = models.TextField(_('description'), blank=True)
    button_text = models.TextField(_('Button text'), max_length=64, blank=True)
    img = StdImageField(_('image'),
                        blank=True,
                        storage=MediaStorage('blocks/insurances/img'),
                        admin_variation='admin',
                        min_dimensions=MIN_DIMENSIONS_INSURANCES,
                        variations=VARIATIONS_INSURANCES,
                        aspects='normal',
                        crop_area=True,
                        )
    
    class Meta:
        verbose_name = _('Insurances')
        verbose_name_plural = _('Insurances')


class AppointmentBlock(AttachableBlock):
    BLOCK_VIEW = 'blocks.views.appointment_block_render'
    
    header = models.CharField(_('header'), max_length=128, blank=True)
    description = models.TextField(_('description'), blank=True)
    btn_text = models.TextField(_('Button text'), max_length=64, blank=True)
    btn_link = models.TextField(_('custom button link'), blank=True)
    
    class Meta:
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointment')


class ShareBlock(AttachableBlock):
    BLOCK_VIEW = 'blocks.views.share_block_render'
    like_slogan = models.CharField(_('like slogan'), max_length=128, blank=True)
    
    class Meta:
        verbose_name = _('Share')
        verbose_name_plural = _('Share')


class WhyChooseUsBlock(AttachableBlock):
    BLOCK_VIEW = 'blocks.views.why_block_render'
    header = models.CharField(_('header'), max_length=128, blank=True)
    
    class Meta:
        verbose_name = _('Why Choose Us')
        verbose_name_plural = _('Why Choose Us')


class Advantages(models.Model):
    config = models.ForeignKey(WhyChooseUsBlock, related_name='advantages', default=True, blank=True)
    ICONS = (
        ('holistic', (0, -87)),
        ('specialization', (-34, -87)),
        ('insurance', (-68, -87)),
    )
    icon = SpriteImageField(_('icon'),
                            sprite='img/sprite.svg',
                            size=(34, 34),
                            choices=ICONS,
                            default=ICONS[0][0],
                            )
    title = models.CharField(_('title'), max_length=128, blank=True)
    description = models.TextField(_('description'), blank=True)
    sort_order = models.PositiveIntegerField(_('order'), default=0)
    
    class Meta:
        verbose_name = _("Advantage")
        verbose_name_plural = _('Advantages')
        ordering = ('sort_order',)
    
    def __str__(self):
        return self.title


class FocusOnBlock(AttachableBlock):
    BLOCK_VIEW = 'blocks.views.focus_on_block_render'
    header = models.CharField(_('header'), max_length=128, blank=True)
    
    class Meta:
        verbose_name = _('Focus On')
        verbose_name_plural = _('Focus On')


class Focuses(models.Model):
    config = models.ForeignKey(FocusOnBlock, related_name='focuses', default=True, blank=True)
    ICONS = (
        ('auto-accident', (0, -87)),
        ('work-comp', (-34, -87)),
        ('sports', (-68, -87)),
        ('slip-and-falls', (-68, -87)),
        ('personal', (-68, -87)),
    )
    icon = SpriteImageField(_('icon'),
                            sprite='img/sprite.svg',
                            size=(34, 34),
                            choices=ICONS,
                            default=ICONS[0][0],
                            )
    title = models.CharField(_('title'), max_length=128, blank=True)
    sort_order = models.PositiveIntegerField(_('order'), default=0)
    
    class Meta:
        verbose_name = _("Focus On")
        verbose_name_plural = _('Focus On')
        ordering = ('sort_order',)
    
    def __str__(self):
        return self.title


class SliderImageItem(GalleryImageItem):
    STORAGE_LOCATION = 'blocks/our_mission/slider'
    MIN_DIMENSIONS = MIN_DIMENSIONS_SLIDER
    VARIATIONS = VARIATIONS_SLIDER
    ADMIN_VARIATION = 'admin'
    
    ADMIN_CLIENT_RESIZE = True
    
    ASPECTS = 'desktop'
    SHOW_VARIATION = None


class Slider(GalleryBase):
    IMAGE_MODEL = SliderImageItem


class OurMissionBlock(AttachableBlock):
    BLOCK_VIEW = 'blocks.views.our_mission_block_render'
    slider = GalleryField(Slider, verbose_name=_('slider'), blank=True, null=True)
    
    header = models.CharField(_('header'), max_length=128, blank=True)
    description = models.TextField(_('description'), blank=True)
    
    class Meta:
        verbose_name = _('Our Mission')
        verbose_name_plural = _('Our Mission')


class PartnersBlock(AttachableBlock):
    BLOCK_VIEW = 'blocks.views.partners_block_render'
    header = models.CharField(_('header'), max_length=128, blank=True)
    
    class Meta:
        verbose_name = _('Partners')
        verbose_name_plural = _('Partners')


class Partners(models.Model):
    config = models.ForeignKey(PartnersBlock, related_name='partners', default=True, blank=True)
    img = ImageField(_('image'), storage=MediaStorage('blocks/partners/img'), blank=True)
    link = models.URLField(_('partner link'), blank=True)
    sort_order = models.PositiveIntegerField(_('order'), default=0)
    
    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _('Partners')
        ordering = ('sort_order',)
    
    def __str__(self):
        return str(self.img)[2:]


class BlogBlock(AttachableBlock):
    BLOCK_VIEW = 'blocks.views.blog_block_render'
    header = models.CharField(_('header'), max_length=128, blank=True)
    
    class Meta:
        verbose_name = _('Blog Post')
        verbose_name_plural = _('Blog Posts')


class ServiceBlock(AttachableBlock):
    BLOCK_VIEW = 'blocks.views.service_block_render'
    header = models.CharField(_('header'), max_length=128, blank=True)
    
    class Meta:
        default_permissions = ()
        verbose_name = _('Services')
        verbose_name_plural = _('Services')


class ContactBlock(AttachableBlock):
    BLOCK_VIEW = 'blocks.views.contact_block_render'
    
    header = models.CharField(_('header'), max_length=128, blank=True)
    
    consultation_title = models.CharField(_('consultation title'), max_length=16, blank=True)
    consultation_btn_text = models.CharField(_('consultation btn text'), max_length=64, blank=True)
    
    class Meta:
        default_permissions = ()
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
