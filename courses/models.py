from django.db import models

class Base(models.Model):
    publication = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

    def __str__(self):
        return self.title


class Review(Base):
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default = '')
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = "Avaliações"
        unique_together = ['email', 'course']
        ordering = ['id']

    def __str__(self):
        return f'{self.name} avaliou o curso {self.course} com nota {self.rating}'
