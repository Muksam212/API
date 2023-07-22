from rest_framework import serializers
from user.models import User

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "confirm_password"
        )
        extra_kwargs = {
            "password":{"write_only":True},
        }

    def validate(self, data):
        pwd = data.get("password")
        cf_pwd = data.get("confirm_password")

        if pwd != cf_pwd:
            raise serializers.ValidationError("Password did not match")
        return data
    
    def validate_email(self, value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError("Email already exists. Please enter another one")
        return value
    
    def create(self, validate_data):
        validate_data.pop("confirm_password", None)
        return User.objects.create_user(**validate_data)
    

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ("email","password")

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","email","username")


class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ("password","confirm_password")
    
    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        user = self.context.get("user")

        if password != confirm_password:
            raise serializers.ValidationError("Password and Confirm password didn't match")
        user.set_password(password)
        user.save()
        return attrs
