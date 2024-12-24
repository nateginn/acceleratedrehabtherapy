from django import forms


class SpriteImageWidget(forms.Widget):
    template_name = 'sprite_image/admin/widget.html'

    class Media:
        css = {
            'all': (
                'sprite_image/admin/css/sprite_image.css',
            )
        }
        js = (
            'sprite_image/admin/js/sprite_image.js',
        )

    def __init__(self, *args, sprite='', size=(), background='#FFFFFF', **kwargs):
        self.sprite = sprite
        self.size = size
        self.background = background
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        choices = tuple(self.choices)
        choices_dict = dict(choices)

        context = super().get_context(name, value, attrs)
        context.update({
            'size': self.size,
            'sprite': self.sprite,
            'background': self.background,
            'choices': choices,
            'initial_position': choices_dict.get(str(value), (0, 0)),
        })
        return context
