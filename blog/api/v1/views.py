from .serializers import PostSerializer
from blog.models import Post

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def Post_List_Api_View(request) :
    if request.method == 'GET' :
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(request.data)
        else :
            return Response(serializer.errors)