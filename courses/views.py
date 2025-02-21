from rest_framework.generics import get_object_or_404
from rest_framework import generics

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import permissions

from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer
from .permissions import IsSuperUser

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

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser, permissions.DjangoModelPermissions,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size=1
        reviews = Review.objects.filter(course_id=pk)
        page = self.paginate_queryset(reviews)
        
        if page is not None:
            serializer = ReviewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(ReviewSerializer(reviews, many=True).data)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

