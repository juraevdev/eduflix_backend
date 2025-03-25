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
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['role'] = 'admin'
            name = serializer.validated_data['name']
            password = serializer.validated_data['password']

            admin = CustomUser.objects.filter(name=name).first()
            if admin is None:
                return Response({'message': 'admin not found!'}, status=status.HTTP_404_NOT_FOUND)

            if not admin.check_password(password):
                return Response({'message': 'Wrong password, please try again'}, status=status.HTTP_401_UNAUTHORIZED)
            
            if admin.role != "admin":
                return Response({"message": "You're not admin!"}, status=status.HTTP_403_FORBIDDEN)

            refresh = RefreshToken.for_user(admin)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ManagerRegisterApiView(generics.GenericAPIView):
    serializer_class = CustomUserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['role'] = 'manager'
            serializer.save()
            return Response(
                {
                    "message": "Manager registered successfully!",
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagerLoginApiView(generics.GenericAPIView):
    serializer_class = CustomUserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.save(raise_exception=True):
            serializer.validated_data['role'] = 'manager'
            name = serializer.validated_data['name']
            password = serializer.validated_data['password']

            manager = CustomUser.objects.filter(name=name).first()
            if manager is None:
                return Response({'message': 'Manager not found!'}, status=status.HTTP_404_NOT_FOUND)
            
            if manager.role != "manager":
                return Response({"message": "You're not manager!"}, status=status.HTTP_403_FORBIDDEN)

            if not manager.check_password(password):
                return Response({'message': 'Wrong password, please try again!'}, status=status.HTTP_401_UNAUTHORIZED)

            refresh = RefreshToken.for_user(manager)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AccountantRegisterApiView(generics.GenericAPIView):
    serializer_class = CustomUserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['role'] = 'accountant'
            serializer.save()
            return Response({
                "message": "Accountant registered successfully!"
            },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountantLoginApiView(generics.GenericAPIView):
    serializer_class = CustomUserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['role'] = 'accountant'
            name = serializer.validated_data['name']
            password = serializer.validated_data['password']

            accountant = CustomUser.objects.filter(
                name=name, role='accountant').first()
            if accountant is None:
                return Response({"message": "Accountant not found!"}, status=status.HTTP_404_NOT_FOUND)

            if accountant.role != 'accountant':
                return Response({"message": "You're not accountant!"}, status=status.HTTP_403_FORBIDDEN)

            if not accountant.check_password(password):
                return Response({"message": "Wrong password, please try again!"}, status=status.HTTP_401_UNAUTHORIZED)

            refresh = RefreshToken.for_user(accountant)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)