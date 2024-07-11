from django.urls import path

from well.apps import WellConfig
from rest_framework.routers import DefaultRouter

from lesson.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = WellConfig.name

urlpatterns = [
    path('', LessonListAPIView.as_view(), name='list'),
    path('/create/', LessonCreateAPIView.as_view(), name='create'),
    path('retrieve/<int:pk>/', LessonRetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update'),
    path('destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='destroy'),
]
