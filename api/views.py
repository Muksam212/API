from .serializers import UserSerializer

from rest_framework.generics import GenericAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from user.models import User

from .renderers import UserRenderer

from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh":str(refresh),
        "access":str(refresh.access_token)
    }


class RegisterAPIView(GenericAPIView):
    serializer_class = UserSerializer
    renderer_classes = [UserRenderer]

    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_token_for_user(user)
            return Response({"msg":"Registration Created","token":token}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class RegisterListAPIView(ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all().order_by("-created_at")
    

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class RegisterDeleteAPIView(APIView):
    def delete(self, request, id = None):
        user = get_object_or_404(User, id = id)
        user.delete()
        return Response({"message":"deleted"})
    

from .serializers import UserLoginSerializer
from django.contrib.auth import authenticate
class LoginAPIView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format = None):
        serializer = UserLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        password = serializer.data.get("password")
        usr = authenticate(email=email, password=password)
        if usr is not None:
            tokens = get_token_for_user(usr)
            return Response({"msg":"Login Successful","token":tokens}, status = status.HTTP_201_CREATED)
        return Response({"error":"Email or Password is Incorrect"}, status = status.HTTP_400_BAD_REQUEST)
    
from rest_framework.permissions import IsAuthenticated

class UserProfileAPIView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format = None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

from .serializers import UserChangePasswordSerializer
class UserChangePasswordAPIView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format = None):
        serializer = UserChangePasswordSerializer(data = request.data, context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({"msg":"Password Change Successfully"}, status = status.HTTP_200_OK)