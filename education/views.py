from rest_framework import generics, status
from rest_framework.response import Response
from accounts.permissions import IsManager, IsAdmin
from education.models import School, EduCenter
from education.serializers import SchoolSerializer, EduCenterSerializer



class SchoolCreateApiView(generics.GenericAPIView):
    serializer_class = SchoolSerializer
    permission_classes = [IsAdmin]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'School created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class EduCenterCreateApiView(generics.GenericAPIView):
    serializer_class = EduCenterSerializer
    permission_classes = [IsAdmin]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Education center created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SchoolListApiView(generics.GenericAPIView):
    serializer_class = SchoolSerializer

    def get(self, request):
        school = School.objects.all()
        serializer = self.get_serializer(school, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class EduCenterListApiView(generics.GenericAPIView):
    serializer_class = EduCenterSerializer

    def get(self, request):
        educenter = EduCenter.objects.all()
        serializer = self.get_serializer(educenter, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)