from rest_framework import generics, status
from rest_framework.response import Response
from accounts.permissions import IsManager, IsAdmin
from education.models import School, EduCenter
from education.serializers import SchoolSerializer, EduCenterSerializer

class SchoolCreateApiView(generics.GenericAPIView):
    serializer_class = SchoolSerializer
    permission_classes = [IsManager]

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
    