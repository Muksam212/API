from ..urls.author import urlpatterns as author_urlpatterns
from ..urls.blog import urlpatterns as blog_urlpatterns

from django.urls import path, include

urlpatterns = [
    path("", include(author_urlpatterns)),
    path("", include(blog_urlpatterns))
]
