from rest_framework import serializers
from app_accounts.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):

    role = serializers.ReadOnlyField(source="role.name")
    print(role)

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email",
                  "role", "username")


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom fields
        user_data = UserSerializer(user).data
        for key, value in user_data.items():
            if key != "id":
                token[key] = value
        return token


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    role = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email",
                  "role", "username", 'password',)
