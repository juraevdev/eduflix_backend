from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.serializers import CustomUserRegisterSerializer, CustomUserLoginSerializer
from accounts.models import CustomUser

class CustomUserRegisterApiView(generics.GenericAPIView):
    serializer_class = CustomUserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['role'] = 'admin'
            serializer.save()
            return Response(
                {"message": "Admin registered successfully!", "data": serializer.data},
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomUserLoginApiView(generics.GenericAPIView):
    serializer_class = CustomUserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.validated_data['role'] = 'admin'
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            admin = CustomUser.objects.filter(email=email).first()
            if admin is None:
                return Response({'message': 'admin not found!'}, status=status.HTTP_404_NOT_FOUND)
            
            if not admin.check_password(password):
                return Response({'message': 'Wrong password, please try again'}, status=status.HTTP_401_UNAUTHORIZED)
            
            refresh = RefreshToken.for_user(admin)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    