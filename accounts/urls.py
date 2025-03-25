from django.urls import path
from accounts.views import (
    CustomUserRegisterApiView, CustomUserLoginApiView, 
    ManagerRegisterApiView, ManagerLoginApiView, 
    AccountantRegisterApiView, AccountantLoginApiView
)

urlpatterns = [
    path('admin/register/', CustomUserRegisterApiView.as_view()),
    path('admin/login/', CustomUserLoginApiView.as_view()),
    path('manager/register/', ManagerRegisterApiView.as_view()),
    path('manager/login/', ManagerLoginApiView.as_view()),
    path('accountant/register/', AccountantRegisterApiView.as_view()),
    path('accountant/login/', AccountantLoginApiView.as_view()),
]