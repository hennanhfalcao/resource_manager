from django.contrib import admin

from .models import Course, Review

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'publication', 'active']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'email', 'comment', 'publication', 'update', 'rating', 'active']