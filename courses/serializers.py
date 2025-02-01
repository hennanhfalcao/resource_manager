from rest_framework import serializers

from courses.models import Course, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }

        model = Review
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'publication',
            'active',
        )
        
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'publication',
            'active',
        )