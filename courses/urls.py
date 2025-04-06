from django.urls import path
from courses.views import (
    CourseCreateApiView, CourseListApiView,
    CourseDeleteAPiView, CourseDetailApiView,
    GroupCreateApiView, GroupListApiView,
    GroupDeleteApiView, GroupDetailApiView,
    AssignTeacherToGroupApiView, AssignPupilToGroupApiView,
    DeleteTeacherFromGroupApiView, DeletePupilFromGroupApiView
)

urlpatterns = [
    path('course/create/', CourseCreateApiView.as_view()),
    path('course/all/', CourseListApiView.as_view()),
    path('course/delete/<int:id>/', CourseDeleteAPiView.as_view()),
    path('course/detail/<int:id>/', CourseDetailApiView.as_view()),
    path('group/create/', GroupCreateApiView.as_view()),
    path('group/all/', GroupListApiView.as_view()),
    path('group/delete/<int:id>/', GroupDeleteApiView.as_view()),
    path('group/detail/<int:id>/', GroupDetailApiView.as_view()),
    path('assign/teacher/', AssignTeacherToGroupApiView.as_view()),
    path('assign/pupil/', AssignPupilToGroupApiView.as_view()),
    path('remove/teacher-group/', DeleteTeacherFromGroupApiView.as_view()),
    path('remove/pupil-group/', DeletePupilFromGroupApiView.as_view()),
]