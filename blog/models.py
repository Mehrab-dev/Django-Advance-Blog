from django.db import models
from django.urls import reverse


class Post(models.Model) :
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=True)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey('account.Profile',on_delete=models.CASCADE,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def get_snippet(self) :
        return self.content[:10] + '....'
    
    def get_relative_api_url(self) :
        return reverse('blog:api-v1:post_detail_modelviewset',kwargs={'pk':self.id})
    
class Category(models.Model) :
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name