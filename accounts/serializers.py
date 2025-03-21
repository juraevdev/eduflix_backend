from rest_framework import serializers
from accounts.models import CustomUser

class CustomUserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ("name", "email", "role")
        extra_kwargs = {"password": {"write_only": True}, "confirm_password": {"write_only": True}}

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Password didn't match")
        return data
    
    def create(self, validated_data):
        role = validated_data.pop("role")
        user = CustomUser.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            role = role,
        )
        return user
    
class CustomUserLoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()