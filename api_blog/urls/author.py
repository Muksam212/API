from ..views.author import AuthorListAPIView, AuthorDetailsAPIView
from django.urls import path

urlpatterns = [
    path("api/author/list/create/", AuthorListAPIView.as_view(), name="api_author_create"),
    path("api/author/update/<int:id>/delete/", AuthorDetailsAPIView.as_view(), name="api_author_details"),
]
