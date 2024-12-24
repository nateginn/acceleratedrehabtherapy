from base_page.views import BasePageSingletonView
from .models import MainPageConfig


class IndexView(BasePageSingletonView):
    model = MainPageConfig
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'is_main_page': True,
        })
        
        return context
