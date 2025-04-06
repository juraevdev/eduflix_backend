from django.urls import path
from accounts.views import (
    CustomUserRegisterApiView, CustomUserLoginApiView, 
    ManagerRegisterApiView, ManagerLoginApiView, 
    AccountantRegisterApiView, AccountantLoginApiView,
    TeacherRegisterApiView, TeacherLoginApiView,
    PupilRegisterApiView, PupilLoginApiView,
    PasswordResetRequestApiView, PasswordResetVerifyApiView, PasswordResetApiView
)

urlpatterns = [
    path('admin/register/', CustomUserRegisterApiView.as_view()),
    path('admin/login/', CustomUserLoginApiView.as_view()),
    path('manager/register/', ManagerRegisterApiView.as_view()),
    path('manager/login/', ManagerLoginApiView.as_view()),
    path('accountant/register/', AccountantRegisterApiView.as_view()),
    path('accountant/login/', AccountantLoginApiView.as_view()),
    path('teacher/register/', TeacherRegisterApiView.as_view()),
    path('teacher/login/', TeacherLoginApiView.as_view()),
    path('pupil/register/', PupilRegisterApiView.as_view()),
    path('pupil/login/', PupilLoginApiView.as_view()),
    path('admin/password/reset-request/', PasswordResetRequestApiView.as_view()),
    path('admin/password/reset-verify/', PasswordResetVerifyApiView.as_view()),
    path('admin/password/reset/', PasswordResetApiView.as_view()),
]