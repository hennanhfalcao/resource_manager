from rest_framework.generics import get_object_or_404
from rest_framework import generics

from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer


"""
API V1
"""

class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ReviewsAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()

class ReviewAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                    course_id=self.kwargs.get('curso_pk'),
                                    pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
    

"""
API V2
"""

class CourseViewSet(NestedViewSetMixin,viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ReviewViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer