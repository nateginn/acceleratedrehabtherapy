from django.http import Http404
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.detail import BaseDetailView

from seo.models import SeoConfig
from seo.seo import Seo


class BasePageDetailView(TemplateResponseMixin, BaseDetailView):
    context_object_name = 'config'
    template_name = 'base_page/index.html'
    
    def get_seo(self):
        seo = Seo()
        seo.set_data(self.object, defaults={
            'title': '%s | %s' % (self.object.title, SeoConfig.get_solo().company_name),
            'og_title': self.object.title,
        })
        return seo
    
    def get_context_data(self, **kwargs):
        if not getattr(self.get_object(), 'visible', True):
            raise Http404
        
        self.breadcrumbs()
        
        seo = self.get_seo()
        seo.save(self.request)
        
        context = super().get_context_data(**kwargs)
        
        return context
    
    def breadcrumbs(self):
        if hasattr(self.object, 'parent_singleton'):
            self.request.breadcrumbs.add(self.object.title)
        
        if hasattr(self.object, 'get_ancestors'):
            for ancestor in self.object.get_ancestors():
                self.request.breadcrumbs.add(ancestor)
        
        self.request.breadcrumbs.add(self.object.title)


class BasePageSingletonView(BasePageDetailView):
    def get_object(self, queryset=None):
        return self.model.get_solo()
