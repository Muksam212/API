from rest_framework import serializers
from blog.models import Blog, Author

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset = Author.objects.all(), many = False)
    class Meta:
        model = Blog
        fields = (
            "id",
            "title",
            "content",
            "author",
            "views_count"
        )