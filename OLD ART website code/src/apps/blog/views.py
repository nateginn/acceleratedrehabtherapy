from django.http.response import Http404
from django.shortcuts import resolve_url

from base_page.views import BasePageDetailView, BasePageSingletonView
from paginator.paginator import Paginator, EmptyPage
from paginator.utils import get_paginator_meta
from seo.models import SeoConfig
from seo.seo import Seo
from .models import BlogConfig, BlogPost
from django.utils.timezone import now


class IndexView(BasePageSingletonView):
    model = BlogConfig
    template_name = 'blog/index.html'
    
    def get_context_data(self, **kwargs):
        posts = BlogPost.objects.visible()
        
        try:
            paginator = Paginator(
                self.request,
                object_list=posts,
                per_page=8,
                page_neighbors=1,
                side_neighbors=1,
                allow_empty_first_page=True,
            )
        except EmptyPage:
            raise Http404
        
        seo = Seo()
        seo.set(get_paginator_meta(paginator))
        seo.set_data(self.object, defaults={
            'title': '%s | %s' % (self.object.title, SeoConfig.get_solo().company_name),
            'og_title': self.object.title,
        })
        
        # Unique title
        title_appends = ' | '.join(map(str, filter(bool, [
            'Page %d/%d' % (paginator.current_page_number, paginator.num_pages)
            if paginator.current_page_number >= 2 else '',
        ])))
        if title_appends:
            default_title = seo.title.popleft()
            seo.title = '%s | %s' % (default_title, title_appends)
            seo.description = ''
        seo.save(self.request)
        
        context = super().get_context_data(**kwargs)
        context.update({
            'config': self.object,
            'paginator': paginator,
        })
        return context


class BlogDetailView(BasePageDetailView):
    model = BlogPost
    template_name = 'base_page/index.html'
    
    def get_context_data(self, **kwargs):
        if self.object.status == 1 or self.object.date >= now():
            raise Http404
        
        self.request.breadcrumbs.add(BlogConfig.get_solo().title, resolve_url('blog:index'))
        
        context = super().get_context_data(**kwargs)
        context.update({
            'is_blog': True,
        })
        return context
