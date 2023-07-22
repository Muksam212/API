from .import views
from django.urls import path

urlpatterns = [
    path("api/register/", views.RegisterAPIView.as_view(), name="register"),
    path("api/register/list/", views.RegisterListAPIView.as_view(), name="list"),

    #delete register
    path("api/register/<int:id>/delete/", views.RegisterDeleteAPIView.as_view(), name="delete"),

    path("api/login/", views.LoginAPIView.as_view(), name="login"),
    path('api/user/profile/view/', views.UserProfileAPIView.as_view(), name="profile_view"),
    path('api/user/change/password/', views.UserChangePasswordAPIView.as_view(), name="password_change")

]
