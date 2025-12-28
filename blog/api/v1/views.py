from .serializers import PostSerializer , CategorySerializer
from blog.models import Post , Category
from django.shortcuts import get_object_or_404
from .paginations import DefaultPaginations

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView , ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter , SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

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
"""
        

"""
class PostDetail(RetrieveUpdateDestroyAPIView) :
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
"""

    
class PostViewSet(viewsets.ViewSet) :
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self,request) :
        serializer = PostSerializer(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None) :
        post = get_object_or_404(self.queryset,pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def create(self,request,pk=None) :
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(request.data)
        else :
            return Response(serializer.errors)

    def update(self,request,pk=None) :
        post = get_object_or_404(Post,pk=pk)
        serializer = self.serializer_class(post,data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(request.data)
        else :
            return Response(serializer.data)
        
    def destroy(self,request,pk=None) :
        post = get_object_or_404(Post,pk=pk)
        post.delete()
        return Response ({'detail':'item removes successfully'})
    
    
class PostModelViewSet(viewsets.ModelViewSet) :
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    # filterset_fields = ['author','status']
    filterset_fields = {'category':['exact','in'],'author':['exact','in']}
    search_fields = ['title']
    ordering_fields = ['published_date']
    pagination_class = DefaultPaginations


class CategoryModelViewSet(viewsets.ModelViewSet) :
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

