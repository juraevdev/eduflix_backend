from rest_framework import generics, status
from rest_framework.response import Response
from courses.models import Course, Group
from courses.serializers import CourseSerializer, CourseDetailSerializer, GroupSerializer, AssignTeacherToGroupSerializer, AssignPupilToGroupSerializer
from accounts.permissions import IsAdmin, IsManager
from accounts.models import CustomUser


class CourseCreateApiView(generics.GenericAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAdmin]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Course created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class CourseListApiView(generics.GenericAPIView):
    serializer_class = CourseDetailSerializer

    def get(self, request):
        course = Course.objects.all()
        serializer = self.get_serializer(course, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CourseDeleteAPiView(generics.GenericAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAdmin]

    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response({'message': 'Course deleted'}, status=status.HTTP_200_OK)


class CourseDetailApiView(generics.GenericAPIView):
    serializer_class = CourseSerializer

    def get(self, request, id):
        course = Course.objects.get(id=id)
        serializer = self.get_serializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GroupCreateApiView(generics.GenericAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAdmin]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Group created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class GroupListApiView(generics.GenericAPIView):
    serializer_class = GroupSerializer

    def get(self, request):
        group = Group.objects.all()
        serializer = self.get_serializer(group, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class GroupDeleteApiView(generics.GenericAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAdmin]

    def delete(self, request, id):
        group = Group.objects.get(id=id)
        group.delete()
        return Response({'message': 'Group deleted'}, status=status.HTTP_200_OK)
    

class GroupDetailApiView(generics.GenericAPIView):
    serializer_class = GroupSerializer

    def get(self, request, id):
        group = Group.objects.get(id=id)
        serializer = self.get_serializer(group)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AssignTeacherToGroupApiView(generics.GenericAPIView):
    serializer_class = AssignTeacherToGroupSerializer
    permission_classes = [IsAdmin]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        group_id = serializer.validated_data['group_id']
        teacher_id = serializer.validated_data['teacher_id']
        role = serializer.validated_data['role']

        try: 
            group = Group.objects.get(id=group_id)
            user = CustomUser.objects.get(id=teacher_id)
        except (Group.DoesNotExist, CustomUser.DoesNotExist):
            return Response({'error': 'Group or teacher not found!'}, status=status.HTTP_404_NOT_FOUND)
        
        if role == 'teacher':
            group.teachers.add(user)

        return Response({'message': f"{user.name} added to group!"}, status=status.HTTP_200_OK)


class AssignPupilToGroupApiView(generics.GenericAPIView):
    serializer_class = AssignPupilToGroupSerializer
    permission_classes = [IsAdmin]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        group_id = serializer.validated_data['group_id']
        pupil_id = serializer.validated_data['pupil_id']
        role = serializer.validated_data['role']

        try: 
            group = Group.objects.get(id=group_id)
            user = CustomUser.objects.get(id=pupil_id)
        except (Group.DoesNotExist, CustomUser.DoesNotExist):
            return Response({'error': 'Group or pupil not found!'}, status=status.HTTP_404_NOT_FOUND)
        
        if role == 'pupil':
            group.pupils.add(user)

        return Response({'message': f"{user.name} added to group!"}, status=status.HTTP_200_OK)
    

class DeleteTeacherFromGroupApiView(generics.GenericAPIView):
    serializer_class = AssignTeacherToGroupSerializer
    permission_classes = [IsAdmin]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        group_id = serializer.validated_data['group_id']
        teacher_id = serializer.validated_data['teacher_id']
        role = serializer.validated_data['role']

        try:
            group = Group.objects.get(id=group_id)
            user = CustomUser.objects.get(id=teacher_id)
        except (Group.DoesNotExist, CustomUser.DoesNotExist):
            return Response({'message': 'Group or teacher not found!'}, status=status.HTTP_404_NOT_FOUND)
        
        if role == 'teacher':
            group.teachers.remove(user)

        return Response({'message': f"{user.name} removed from group!"}, status=status.HTTP_200_OK)
    


class DeletePupilFromGroupApiView(generics.GenericAPIView):
    serializer_class = AssignPupilToGroupSerializer
    permission_classes = [IsAdmin]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        group_id = serializer.validated_data['group_id']
        pupil_id = serializer.validated_data['pupil_id']
        role = serializer.validated_data['role']

        try:
            group = Group.objects.get(id=group_id)
            user = CustomUser.objects.get(id=pupil_id)
        except (Group.DoesNotExist, CustomUser.DoesNotExist):
            return Response({'error': 'Group or teacher not found!'}, status=status.HTTP_404_NOT_FOUND)
        
        if role == 'pupil':
            group.pupils.remove(user)

        return Response({'message': f"{user.name} removed from group!"}, status=status.HTTP_200_OK)