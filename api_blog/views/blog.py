from ..serializers.blog import BlogSerializer
from blog.models import Blog, Author

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class BlogList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        author_id = self.kwargs["id"]
        try:
            author = Author.objects.get(id = author_id)
            blog = Blog.objects.filter(author = author)
            serializer = BlogSerializer(blog, many = True)
            return Response(serializer.data)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=404)

    def post(self, request):
        serializer = BlogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Blog created successful"}, status = status.HTTP_201_CREATED)
        return Response({"errors":"Failed"}, status.HTTP_400_BAD_REQUEST)

from django.shortcuts import get_object_or_404

class BlogDetails(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        blog_id = kwargs.get("id")
        try:
            blog = Blog.objects.get(id = blog_id)
            blog.views_count += 1
            blog.save()
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        except Blog.DoesNotExist:
            return Response({"error":"Blog not found"}, status = status.HTTP_204_NO_CONTENT)
        
    def put(self, request, id = None):
        blog = get_object_or_404(Blog, id = id)
        serializer = BlogSerializer(blog, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Update Successful"}, status = status.HTTP_201_CREATED)
        return Response({"errors":"Failed"}, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id = None):
        blog = get_object_or_404(Blog, id = id)
        serializer = BlogSerializer(blog, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Update Successful"}, status = status.HTTP_201_CREATED)
        return Response({"errors":"Failed"}, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id = None):
        blog = get_object_or_404(Blog, id = id)
        blog.delete()
        return Response({"msg":"Deleted"})