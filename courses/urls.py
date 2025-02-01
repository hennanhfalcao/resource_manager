from django.urls import path

from .views import CourseAPIView, ReviewAPIView

urlpatterns = [
    path('cursos/', CourseAPIView.as_view(), name='course-list'),
    path('avaliacoes/', ReviewAPIView.as_view(), name='review-list'),
]