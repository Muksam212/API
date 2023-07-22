from ..serializers.author import AuthorSerializer
from blog.models import Author

from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from api.renderers import UserRenderer

class AuthorListAPIView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        author = Author.objects.all().filter(user = request.user)
        serializer = AuthorSerializer(author, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg":"Create Success"}, status = status.HTTP_200_OK)
        return Response({"error":"Failed"}, status = status.HTTP_400_BAD_REQUEST)
    

class AuthorDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id = None):
        author = get_object_or_404(Author, id = id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, id = None):
        author = get_object_or_404(Author, id = id)
        serializer = AuthorSerializer(author, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg":"Update Successful"}, status = status.HTTP_201_CREATED)
        return Response({"errors":"Failed To Update"}, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id = None):
        author = get_object_or_404(Author, id = id)
        serializer = AuthorSerializer(author, data = request.data, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg":"Update Successful"}, status = status.HTTP_201_CREATED)
        return Response({"errors":"Failed To Update"}, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id = None):
        author = get_object_or_404(Author, id = id)
        author.delete()
        return Response({"msg":"Delete"}, status = status.HTTP_204_NO_CONTENT)