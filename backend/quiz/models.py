from django.db import models
from user.models import Profile
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        db_table = 'Tag'

    def __str__(self):
        return self.name
    
class Difficulty(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = 'Difficulty'



class Question(models.Model):
    original_language = models.CharField(max_length=255)
    translated_language = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    question_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    
    class Meta:
        db_table = 'Question'

    def __str__(self):
        return f"{self.original_word} - {self.translated_word}"


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    quiz_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Quiz'

class AnswerQuestion(models.Model):
    answer_counter = models.IntegerField(default=0)
    correct_answer = models.IntegerField(default=0)
    wrong_answer = models.IntegerField(default=0)
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    class Meta:
        db_table = 'AnswerQuestion'

class AnswerQuiz(models.Model):
    answer_counter = models.IntegerField(default=0)
    