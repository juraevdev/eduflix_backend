from django.urls import path
from accounts.views import CustomUserRegisterApiView

urlpatterns = [
    path('admin/register/', CustomUserRegisterApiView.as_view()),
]