from django.urls import path
from education.views import SchoolCreateApiView, EduCenterCreateApiView, SchoolListApiView, EduCenterListApiView

urlpatterns = [
    path('school/create/', SchoolCreateApiView.as_view()),
    path('educenter/create/', EduCenterCreateApiView.as_view()),
    path('school/all/', SchoolListApiView.as_view()),
    path('educenter/all/', EduCenterListApiView.as_view()),
]