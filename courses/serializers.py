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
    
    #Nested relatioship
    """reviews = ReviewSerializer(many=True, read_only=True)"""

    #Hyperlinked related field
    """reviews = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='review-detail'
        )"""
    
    #Primary Key Related Field (mais performático)
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'publication',
            'active',
            'reviews',
        )