from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """Topic for categorizing questions"""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    """Stores questions"""

    DIFFICULTY_LEVEL_EASY = "easy"
    DIFFICULTY_LEVEL_MEDIUM = "medium"
    DIFFICULTY_LEVEL_HARD = "hard"

    DIFFICULTY_LEVEL_CHOICES = [
        (DIFFICULTY_LEVEL_EASY, "Easy"),
        (DIFFICULTY_LEVEL_MEDIUM, "Medium"),
        (DIFFICULTY_LEVEL_HARD, "Hard"),
    ]

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    difficulty_level = models.CharField(
        max_length=10, choices=DIFFICULTY_LEVEL_CHOICES, default=DIFFICULTY_LEVEL_EASY
    )

    def __str__(self):
        return self.text


class Choice(models.Model):
    """Multiple choice options for each question"""

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class QuizAttempt(models.Model):
    """Track user attempt for each question"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    date_attempted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.question.text[:30]} - {self.is_correct}"
