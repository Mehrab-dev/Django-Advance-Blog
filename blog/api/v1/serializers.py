from rest_framework import serializers
from blog.models import Post , Category
from django.urls import reverse


# serializer with function
"""
class PostSerializer(serializers.Serializer) :
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
"""

class PostSerializer(serializers.ModelSerializer) :
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_relative_api_url')
    absolute_url = serializers.SerializerMethodField(method_name='get_absolute_url')
    category = serializers.SlugRelatedField(many=False,slug_field='name',queryset = Category.objects.all())

    class Meta :
        model = Post
        fields = ['id','absolute_url','relative_url','title','content','snippet','status','category','author','created_date','updated_date','published_date']
        read_only_fields = ['content']

    def get_absolute_url(self,object) :
        request = self.context.get('request')
        url = reverse('blog:api-v1:post_detail_modelviewset',kwargs={'pk':object.pk})
        return request.build_absolute_uri(url)


    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk') :
            rep.pop('absolute_url',None)
            rep.pop('snippet',None)
        else :
            rep.pop('content',None)

        return rep
        

class CategorySerializer(serializers.ModelSerializer) :

    class Meta :
        model = Category
        fields = ['id','name','created_date']
    