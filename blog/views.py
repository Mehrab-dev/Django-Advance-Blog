from django.views.generic.base import TemplateView , RedirectView
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Post
from .forms import PostForm

class IndexView(TemplateView) :
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'mehrab'
        context['post'] = Post.objects.all()
        return context
    
class RedirectViews(RedirectView) :
    url = "https://www.django-rest-framework.org/"

class PostListView(ListView) :
    # model = Post
    # queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts
    
class PostDetail(DetailView) :
    model = Post
    context_object_name = 'post'

class CreatePost(CreateView) :
    model = Post
    form_class = PostForm
    success_url = '/blog/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class UpdatePost(UpdateView) :
    model = Post
    form_class = PostForm
    success_url = '/blog/posts/'

class DeletePost(DeleteView) :
    model = Post
    success_url = '/blog/posts/'
    context_object_name = 'post'