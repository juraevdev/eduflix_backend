from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import CustomUser, ConfirmationCodes
from accounts.serializers import (
    CustomUserRegisterSerializer, CustomUserLoginSerializer,
    PasswordResetRequestSerializer, PasswordResetVerifySerializer, PasswordResetSerializer
)



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
    
class PasswordResetRequestApiView(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['role'] = 'admin'
            email = serializer.data['email']
            user = CustomUser.objects.filter(email=email).first()
            if user is None:
                return Response({'message': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)
            code = user.generate_verify_code()
            return Response({'message': 'Verification code is sent to your email, Please check inbox!', 'code': code}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PasswordResetVerifyApiView(generics.GenericAPIView):
    serializer_class = PasswordResetVerifySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['role'] = 'admin'
            code = serializer.data['code']
            user = request.user
            otp_code = ConfirmationCodes.objects.filter(code=code).first()

            if user is None:
                return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            
            if otp_code is None:
                return Response({'message': 'Verification code is wrong or expired!'}, status=status.HTTP_401_UNAUTHORIZED)
            
            otp_code.is_used = True
            otp_code.save()
            return Response({'message': 'Verification complete! Now you can change your password'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PasswordResetApiView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['role'] = 'admin'
            email = serializer.data['email']
            new_password = serializer.data['new_password']
            confirm_password = serializer.data['confirm_password']
            user = CustomUser.objects.filter(email=email).first()

            if user is None:
                return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            
            if new_password != confirm_password:
                return Response({"message": "Password didn't match"}, status=status.HTTP_401_UNAUTHORIZED)
            
            user.set_password(confirm_password)
            user.save()
            return Response({'message': 'Password changed successfully!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)