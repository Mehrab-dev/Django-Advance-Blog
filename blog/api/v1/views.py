from .serializers import PostSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView , ListCreateAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

"""
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
"""

"""
class PostList(APIView) :
    serializer_class = PostSerializer

    def get(self,request) :
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    def post(self,request) :
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(request.data)
        else :
            return Response(serializer.errors)
"""


"""
class PostList(GenericAPIView) :
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self,request) :
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request) :
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(request.data)
        else : 
            return Response(serializer.errors)
"""

"""
class PostList(GenericAPIView,ListModelMixin,CreateModelMixin) :
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self,request,*args,**kwargs) :
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs) :
        return self.create(request,*args,**kwargs)
"""


class PostList(ListCreateAPIView) :
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

# post detail
"""
@api_view(['GET','PUT','DELETE'])
def post_detail_api(request,pk) :
    # if request.method == 'GET' :
    #     post = get_object_or_404(Post,pk=pk) 
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)

    try :
        if request.method == 'GET' :
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        elif request.method == 'PUT' :
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post,data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data)
            else :
                return Response(serializer.errors)
        elif request.method == 'DELETE' :
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response({'detail':'item removed successfully'},status=status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist :
        return Response({'detail':'post does not exists'},status=status.HTTP_404_NOT_FOUND)
"""

class PostDetail(APIView) :
    serializer_class = PostSerializer

    def get(self,request,pk) :
        try :
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist :
            return Response({'detail':'post does not exists'},status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,pk) :
        try :
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data)
            else :
                return Response(serializer.errors)
        except Post.DoesNotExist :
            return Response({'detail':'post does not exists'},status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk) :
        try :
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response({'detail':'itrm removed successfully'},status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist :
            return Response({'detail':'post does not exists'})
    

    
