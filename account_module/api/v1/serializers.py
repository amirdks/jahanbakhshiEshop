from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from account_module.models import User


class RegisterSerializer(serializers.ModelSerializer):
    """Registration serializer with password checkup"""

    password = serializers.CharField(
        max_length=68, min_length=8, write_only=True
    )
    password1 = serializers.CharField(
        max_length=68, min_length=8, write_only=True
    )

    class Meta:
        model = User
        fields = ["email", "password", "password1", "avatar"]

    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValidationError(
                {"details": "Passwords does not match"}
            )
        if len(data["password"]) < 8:
            return serializers.ValidationError('رمز عبور نمیتواند کمتر از 8 کارکتر باشد')
        return data

    def create(self, validated_data):
        validated_data.pop("password1")
        return User.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer to manage extra user info"""
    full_name = serializers.ReadOnlyField(source='__str__')
    avatar = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True, required=False)

    # avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        read_only_fields = ["email", "is_superuser", "is_staff", "is_active"]
        fields = [
            "email",
            "full_name",
            "avatar",
            # "avatar_url",
            "first_name",
            "last_name",
            "is_superuser",
            "is_staff",
            "is_active",
        ]

    # def get_avatar_url(self, instance):
    #     request = self.context.get('request')
    #     avatar_url = instance.avatar.url
    #     return request.build_absolute_uri(avatar_url)


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"), write_only=True)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def validate(self, attrs):
        username = attrs.get("email")
        password = attrs.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
            if not user.is_verified:
                raise serializers.ValidationError({"details": "user is not verified"})
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        # if not self.user.is_verified:
        #     raise serializers.ValidationError({"details": "user is not verified"})
        validated_data["email"] = self.user.email
        validated_data["user_id"] = self.user.id
        return validated_data


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, min_length=8)
    new_password = serializers.CharField(required=True, min_length=8)
    new_password1 = serializers.CharField(required=True, min_length=8)

    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("new_password1"):
            raise serializers.ValidationError(
                {"detail": "new_password with new_password1 is not match"}
            )
        # try:
        #     validate_password(attrs.get("new_password"))
        # except exceptions.ValidationError as e:
        #     raise serializers.ValidationError({"new_password": list(e.messages)})
        return super().validate(attrs)
