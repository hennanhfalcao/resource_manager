from rest_framework import serializers
from django.db.models import Avg

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
        
    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError('A avaliação deve ser um inteiro entre 1 e 5')
        return value

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

    #average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'publication',
            'active',
            'reviews',
            'average_rating'
        )

    """def get_average_rating(self, obj):    
        average = obj.reviews.aggregate(Avg('rating')).get('rating__avg')
        if average is None:
            return 0
        return round(average*2)/2"""