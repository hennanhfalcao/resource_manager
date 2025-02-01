from django.urls import path

from .views import CourseAPIView, CoursesAPIView, ReviewAPIView, ReviewsAPIView

urlpatterns = [
    path('cursos/', CoursesAPIView.as_view(), name='courses'),
    path('avaliacoes/', ReviewsAPIView.as_view(), name='reviews'),
    path('cursos/<int:pk>/', CourseAPIView.as_view(), name='course'),
    path('avaliacoes/<int:pk>/', ReviewAPIView.as_view(), name='review'),
]