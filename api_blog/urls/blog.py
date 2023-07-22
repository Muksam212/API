from ..views.blog import BlogList,BlogDetails
from django.urls import path

urlpatterns = [
    path("api/blog/list/<int:id>/create/", BlogList.as_view(), name="blog_list"),
    path("api/blog/update/<int:id>/delete/", BlogDetails.as_view(), name="blog_details")
]
