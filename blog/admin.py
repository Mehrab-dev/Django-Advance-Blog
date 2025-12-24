from django.contrib import admin
from .models import Post , Category

class PostAdmin(admin.ModelAdmin) :
    list_display = ['title','status','author','created_date','published_date']
    list_filter = ['status']
    search_fields = ['author']


admin.site.register(Category)
admin.site.register(Post,PostAdmin)