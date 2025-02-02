from django.db.models.signals import post_save, post_delete 
from django.dispatch import receiver
from django.db.models import Avg

from .models import Course, Review


def update_average_rating(course):
    average = course.reviews.aggregate(Avg('rating'))['rating__avg']
    course.average_rating = round(average*2)/2 if average else 0
    course.save()

@receiver(post_save, sender=Review)
def review_saved(sender, instance, **kwargs):
    update_average_rating(instance.course)   


@receiver(post_delete, sender=Review)
def review_deleted(sender, instance, **kwargs):
    update_average_rating(instance.course)