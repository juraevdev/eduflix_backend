from rest_framework import serializers
from accounts.models import CustomUser


class CustomUserRegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=[("admin", "Administrator"), ("manager", "Manager"), ("accountant", "Accountant"), ("teacher", "Teacher"), ("pupil", "Pupil")])
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)


    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Password didn't match")
        return data

    def create(self, validated_data):
        role = validated_data.pop("role")
        user = CustomUser.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            role=role,
            password=validated_data['password']
        )
        return user


class CustomUserLoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()


class AdminProfileSerializer(serializers.Serializer):
    image = serializers.ImageField()
    name = serializers.CharField()
    subject = serializers.CharField()
    subject_cost = serializers.IntegerField()
    cost_share = serializers.IntegerField()
    courses = serializers.CharField()


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.CharField()

class PasswordResetVerifySerializer(serializers.Serializer):
    code = serializers.CharField()

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()

    