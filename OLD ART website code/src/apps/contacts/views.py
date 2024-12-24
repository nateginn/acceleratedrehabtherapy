from ajax_views.decorators import ajax_view
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from base_page.views import BasePageSingletonView
from libs.email import send_template
from .forms import ContactForm
from .models import ContactsConfig, Address
from .models import NotificationReceiver


class IndexView(FormMixin, BasePageSingletonView):
    model = ContactsConfig
    form_class = ContactForm
    template_name = 'contacts/index.html'
    success_url = reverse_lazy('contacts:success')
    
    def get_context_data(self, **kwargs):
        seo = self.get_seo()
        seo.save(self.request)
        
        address = Address.objects.first()
        phone = ''
        
        if address and address.phones:
            phone = address.phones[0]
        
        context = super().get_context_data(**kwargs)
        context.update({
            'addresses': Address.objects.all(),
            'phone': phone,
            'is_contact_page': True
        })
        
        if 'form' not in kwargs:
            context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            print("Form is valid")
            return self.form_valid(form)
        else:
            print("Form is invalid")
            self.object = self.get_object()
            return self.form_invalid(form)
    
    def form_valid(self, form):
        message = form.save()
        receivers = NotificationReceiver.objects.all().values_list('email', flat=True)
        
        print("Receivers:", list(receivers))
        print("Receivers:", receivers)  # Added this line
        
        # Create the email content
        email_content = f"Name: {message.name}\nEmail: {message.email}\nMessage: {message.message}"
        
        # Send email using SendGrid
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        for receiver in receivers:
            email = Mail(
                from_email='casemanager.art@gmail.com',
                to_emails=receiver,
                subject='Message from Contact Form',
                plain_text_content=email_content
            )
            print("Sending email using SendGrid")
            try:
                response = sg.send(email)
                print("Email sent, status code:", response.status_code)
            except Exception as e:
                print("Error sending email:", e)
        
        return super().form_valid(form)


class SuccessView(BasePageSingletonView):
    model = ContactsConfig
    template_name = 'contacts/success.html'
    
    def get_context_data(self, **kwargs):
        address = Address.objects.first()
        phone = ''
        
        if address and address.phones:
            phone = address.phones[0]
        
        context = super().get_context_data(**kwargs)
        context.update({
            'phone': phone
        })
        return context


@ajax_view('contacts.popup')
class MessageView(DetailView):
    model = ContactsConfig
    template_name = 'contacts/popup.html'
    context_object_name = 'config'
    
    def get_object(self, queryset=None):
        return self.model.get_solo()
