from rest_framework import serializers

from ..serializers.blog import BlogSerializer

from blog.models import Author, Blog

class AuthorSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many = True)
    class Meta:
        model = Author
        fields = (
            "id",
            "user",
            "image",
            "gender",
            "blogs"
        )
        depth = 1