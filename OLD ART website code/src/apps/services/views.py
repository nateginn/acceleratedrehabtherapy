from base_page.views import BasePageDetailView
from .models import Service


class DetailView(BasePageDetailView):
    model = Service
    template_name = 'services/detail.html'
    
    def get_context_data(self, **kwargs):
        siblings = self.object.get_siblings(include_self=True).filter(visible=True)
        child = self.object.get_children().filter(visible=True)
        child_node = self.object.is_child_node()
        root = self.object.is_root_node()
        
        seo = self.get_seo()
        seo.save(self.request)
        
        context = super().get_context_data(**kwargs)
        context.update({
            'active': self.object,
            'sub_services': child if root else siblings,
            
            'is_services': True,
            'is_service_page': True if root else False,
            'is_sub_service_page': True if child_node else False
        })
        return context
