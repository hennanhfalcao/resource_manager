from django.urls import path

from .views import CourseAPIView, CoursesAPIView, ReviewAPIView, ReviewsAPIView

urlpatterns = [
    path('cursos/', CoursesAPIView.as_view(), name='courses'),
    path('cursos/<int:pk>/', CourseAPIView.as_view(), name='course'),
    path('cursos/<int:curso_pk>/avaliacoes/', ReviewsAPIView.as_view(), name='course_reviews'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', ReviewAPIView.as_view(), name='course_review'),

    path('avaliacoes/', ReviewsAPIView.as_view(), name='reviews'),
    path('avaliacoes/<int:avaliacao_pk>/', ReviewAPIView.as_view(), name='review'),
]