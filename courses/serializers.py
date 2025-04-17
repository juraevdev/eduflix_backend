from rest_framework import serializers
from courses.models import Course, Group
from accounts.models import CustomUser, CoinHistory, Attendance


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'bio', 'duration', 'fee',
                  'teacher', 'course_type', 'created_at']

    def validate(self, attrs):
        teachers = attrs.get('teacher', [])
        for teacher in teachers:
            if teacher.role != 'teacher':
                raise serializers.ValidationError("Only teachers can be added")
        return attrs


class CustomUserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'role']


class GroupSerializer(serializers.ModelSerializer):
    teachers = CustomUserMiniSerializer(many=True, read_only=True)
    pupils = CustomUserMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'

    def validate(self, attrs):
        teachers = self.initial_data.get('teachers', [])
        for teacher_id in teachers:
            try:
                teacher = CustomUser.objects.get(id=teacher_id)
                if teacher.role != 'teacher':
                    raise serializers.ValidationError(
                        "Only users with role 'teacher' can be added.")
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError(
                    f"User with id {teacher_id} not found.")
        return attrs


class CourseDetailSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(source='courses', many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'bio', 'duration', 'fee',
                  'groups', 'teacher', 'course_type', 'created_at']


class AssignTeacherToGroupSerializer(serializers.Serializer):
    group_id = serializers.IntegerField()
    teacher_id = serializers.IntegerField()
    role = serializers.ChoiceField(choices=["teacher", "Teacher"])


class AssignPupilToGroupSerializer(serializers.Serializer):
    group_id = serializers.IntegerField()
    pupil_id = serializers.IntegerField()
    role = serializers.ChoiceField(choices=["pupil"])


class CoinHistorySerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = CoinHistory
        fields = ['id', 'student', 'action', 'coin', 'created_at']
        read_only_fields = ['coin', 'created_at']

    def get_created_at(self, obj):
        return obj.created_at.strftime("%Y/%m/%d")

    def create(self, validated_data):
        validated_data['teacher'] = self.context['request'].user
        return super().create(validated_data)


class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = ['id', 'student', 'student_name', 'is_present', 'date']
        read_only_fields = ['date']

    
    def get_student_name(self, obj):
        return f'{obj.student.first_name} {obj.student.last_name}'
    

    def create(self, validated_data):
        validated_data['teacher'] = self.context['request'].user
        return super().create(validated_data)