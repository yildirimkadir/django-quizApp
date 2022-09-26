from email.policy import default
from random import choices
from unicodedata import category
from venv import create
from django.db import models

# Create your models here.


class UpdateCreateDate(models.Models):
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


class Quiz(models.Model):
    title = models.CharField(max_length=50, verbose_name="Quiz title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quizzes"


class Question(models.Model):
    SCALE = (
        ('B', 'Beginner')
        ('I', 'Intermediate')
        ('A', 'Advanced')
    )

    title = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.Charfield(max_length=1, choices=SCALE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Option(models.Model):
    option_text = models.Charfield(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_right = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.option_text
