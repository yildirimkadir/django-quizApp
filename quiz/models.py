from unicodedata import category
from venv import create
from django.db import models

# Create your models here.


class UpdateCreateDate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Category Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    @property
    def quiz_count(self):
        return self.quiz_set.count()  # hoca burda related name verip


class Quiz(models.Model):
    title = models.CharField(max_length=50, verbose_name="Quiz title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quizzes"

    @property
    def question_count(self):
        return self.question_set.count()


class Question(models.Model):
    SCALE = (
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )

    title = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=1, choices=SCALE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Option(models.Model):
    option_text = models.CharField(max_length=200)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='options')
    is_right = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.option_text
