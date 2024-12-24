from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from django import forms
from django.utils.translation import ugettext_lazy as _

from libs.form_helper.forms import FormHelperMixin
from libs.widgets import PhoneWidget
from .models import Message


class ContactForm(FormHelperMixin, forms.ModelForm):
    render_label = False
    render_error_message = True
    default_field_template = 'form_helper/unlabeled_field.html'
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible, error_messages={
        'required': _('Error verifying reCAPTCHA, please try again.'),
    })
    
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _('Name'),
            }),
            'phone': PhoneWidget(attrs={
                'placeholder': _('Phone'),
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': _('E-mail'),
            }),
            'message': forms.Textarea(attrs={
                'placeholder': _('Message'),
                'rows': 5,
            })
        }
        error_messages = {
            'name': {
                'required': _('Please enter your name'),
                'max_length': _('Name should not be longer than %(limit_value)d characters'),
            },
            'phone': {
                'invalid': _('Phone field can only contain numbers'),
                'required': _('Please enter your phone'),
                'max_length': _('Phone number should not be longer than %(limit_value)d characters'),
            },
            'email': {
                'invalid': _('Email field can only contain email'),
                'required': _('Please enter your email'),
                'max_length': _('E-mail should not be longer than %(limit_value)d characters'),
            },
            'message': {
                'required': _('Please enter your message'),
                'max_length': _('Message should not be longer than %(limit_value)d characters'),
            },
        }
    
    def clean(self):
        """ Требуем указать email ИЛИ телефон """
        if 'phone' in self.cleaned_data and 'email' in self.cleaned_data:
            phone = self.cleaned_data.get('phone')
            email = self.cleaned_data.get('email')
            
            if not phone and not email:
                self.add_field_error('phone', 'required')
                self.add_field_error('email', 'required')
        
        return super().clean()
