from django.views.generic.base import TemplateView
from .models import Post

class IndexView(TemplateView) :
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'mehrab'
        context['post'] = Post.objects.all()
        return context