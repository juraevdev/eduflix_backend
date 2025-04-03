from django.urls import path
from education.views import SchoolCreateApiView, EduCenterCreateApiView

urlpatterns = [
    path('school/create/', SchoolCreateApiView.as_view()),
    path('educenter/create/', EduCenterCreateApiView.as_view()),
]