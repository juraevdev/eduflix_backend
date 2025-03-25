from rest_framework import serializers
from accounts.models import CustomUser


class CustomUserRegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=[("admin", "Administrator"), ("manager", "Manager"), ("accountant", "Accountant")])
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
    image = serializers.ImageField(upload_to='admin/profile_images/')
    name = serializers.CharField()
    subject = serializers.CharField()
    subject_cost = serializers.IntegerField()
    cost_share = serializers.IntegerField()
    courses = serializers.CharField()
    