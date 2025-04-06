from rest_framework import serializers
from education.models import School, EduCenter
from accounts.permissions import IsManager, IsAdmin

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class EduCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduCenter
        fields = '__all__'

