from django.db import models

from user.models import User
from root.utils import BaseModel
# Create your models here.

GENDER = (
    ("Male","Male"),
    ("Female","Female"),
    ("Other","other")
)

class Author(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="users")
    image = models.ImageField(upload_to="author/images", blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default="Other")

    def __str__(self):
        return f"{self.user.username}"
    


class Blog(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="blogs")
    views_count = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return f"{self.title}"