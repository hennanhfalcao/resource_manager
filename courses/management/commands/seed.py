from django.core.management.base import BaseCommand
from courses.models import Course, Review
from random import choice

class Command(BaseCommand):
    help = 'Seed the database with test data'

    def handle(self, *args, **kwargs):

        courses_data = [
            {"title": "Django para Iniciantes", "url": "https://example.com/django1"},
            {"title": "Django Rest Framework Avançado", "url": "https://example.com/drf2"},
            {"title": "Python para Data Science", "url": "https://example.com/datascience"},
            {"title": "Machine Learning com Python", "url": "https://example.com/machinelearning"},
            {"title": "Desenvolvimento Web com Flask", "url": "https://example.com/flask"},
            {"title": "Banco de Dados Relacional com PostgreSQL", "url": "https://example.com/postgres"},
            {"title": "Arquitetura de Software com Python", "url": "https://example.com/arquitetura"},
            {"title": "Testes Automatizados com PyTest", "url": "https://example.com/pytest"},
            {"title": "Boas Práticas com Clean Code", "url": "https://example.com/cleancode"},
            {"title": "Desenvolvimento Ágil com Scrum", "url": "https://example.com/scrum"},
        ]

        for course in courses_data:
            Course.objects.update_or_create(
                title=course['title'], #Critério de busca;
                defaults = course #Valores padrão para criar ou atualizar;
            )

        self.stdout.write(self.style.SUCCESS('Cursos adicionados com sucesso!'))    

        reviews_data = [
        {"name": "João Silva", "email": "joao@example.com", "comment": "Ótimo curso! Aprendi muito.", "rating": 5},
        {"name": "Maria Souza", "email": "maria@example.com", "comment": "Muito bem explicado, recomendo!", "rating": 4},
        {"name": "Pedro Costa", "email": "pedro@example.com", "comment": "Achei um pouco difícil no começo, mas valeu a pena.", "rating": 4},
        {"name": "Ana Lima", "email": "ana@example.com", "comment": "Gostei da didática do professor.", "rating": 5},
        {"name": "Ricardo Alves", "email": "ricardo@example.com", "comment": "Poderia ter mais exemplos práticos.", "rating": 3},
        {"name": "Juliana Mendes", "email": "juliana@example.com", "comment": "Curso muito básico, esperava mais.", "rating": 2},
        {"name": "Fernando Rocha", "email": "fernando@example.com", "comment": "Me ajudou bastante no trabalho.", "rating": 5},
        {"name": "Camila Duarte", "email": "camila@example.com", "comment": "Vale a pena! Material muito bom.", "rating": 4},
        {"name": "André Gonçalves", "email": "andre@example.com", "comment": "Excelente curso!", "rating": 5},
        {"name": "Lucas Nunes", "email": "lucas@example.com", "comment": "Gostei muito, mas poderia ser mais longo.", "rating": 4},
        {"name": "Carla Xavier", "email": "carla@example.com", "comment": "Me surpreendeu! Ótima didática.", "rating": 5},
        {"name": "Eduardo Tavares", "email": "eduardo@example.com", "comment": "Achei que fosse mais avançado.", "rating": 3},
        {"name": "Sofia Martins", "email": "sofia@example.com", "comment": "Muito conteúdo de qualidade.", "rating": 5},
        {"name": "Guilherme Ribeiro", "email": "guilherme@example.com", "comment": "Esperava mais exercícios práticos.", "rating": 3},
        {"name": "Isabela Fernandes", "email": "isabela@example.com", "comment": "Ótimo para iniciantes!", "rating": 5},
    ]
        
        courses = list(Course.objects.all())
        
        for review in reviews_data:
            course = choice(courses)
            Review.objects.update_or_create(
                course=course,
                email=review['email'],
                defaults=review
            )
        
        self.stdout.write(self.style.SUCCESS('Reviews adicionadas com sucesso!'))