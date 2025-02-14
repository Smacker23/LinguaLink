from django.shortcuts import render
from django.http import JsonResponse
from .models import Tag, Question, Quiz, Difficulty
# Create your views here.


def create_quiz(owner, quiz):
    print("here")
    name = quiz['name'].capitalize()
    quiz_difficulty = quiz['difficulty'].capitalize()
    quiz_tags = quiz['tags']
    quiz_questions = quiz['questions']
    quiz_public = quiz['public']
    original_language = quiz['original_language'].capitalize()
    translated_language = quiz['translated_language'].capitalize()
    quiz = Quiz.objects.filter(name=name, quiz_owner=owner).first()
    if quiz is not None:
        return JsonResponse({'error': 'You already have a quiz with this name'}, status=400)
    quiz_difficulty = Difficulty.objects.filter(name=quiz_difficulty).first()
    quiz = Quiz.objects.create(name=name, difficulty=quiz_difficulty, quiz_owner=owner, public=quiz_public)
    for tag in quiz_tags:
        tag = Tag.objects.get_or_create(name=tag.capitalize())
        quiz.tags.add(tag[0])
    for question in quiz_questions:
        tags = question['tags']
        question_difficulty = Difficulty.objects.filter(name=question['difficulty'].capitalize()).first()
        question = Question.objects.get_or_create(original_language=original_language, translated_language=translated_language,
                                                    question=question['question'].capitalize(), answer=question['answer'].capitalize(), 
                                                  difficulty=question_difficulty, question_owner=owner)
        
        for tag in tags:
            tag = Tag.objects.get_or_create(name=tag.capitalize())
            print(tag)
            question[0].tags.add(tag[0])
        quiz.questions.add(question[0])
    print("final_boss")
    return JsonResponse({'message': 'Quiz created'}, status=200)
    


def get_quizes(owner, name=None):
    data = []  
    if name is not None:
        quizzes = Quiz.objects.filter(name=name, quiz_owner=owner)
        if quizzes is None:
            return JsonResponse({'error': 'Quiz does not exist'}, status=400)
    else:
        quizzes = Quiz.objects.filter(quiz_owner=owner)
        if quizzes is None:
            return JsonResponse({'error': 'You have no quizzes'}, status=400)
    for quiz in quizzes:
        data.append(get_quiz(quiz))  

    return JsonResponse({'quizzes': data}, status=200)  


def get_quiz(quiz):
    questions = [
        {
            'question': q.question,
            'answer': q.answer,
            'difficulty': q.difficulty.name,
            'tags': [tag.name for tag in q.tags.all()]
        }
        for q in quiz.questions.all()
    ]

    return {
        'name': quiz.name,
        'difficulty': quiz.difficulty.name,
        'tags': [tag.name for tag in quiz.tags.all()],
        'questions': questions
    } 


def delete_quiz(owner, quiz):
    quiz = Quiz.objects.filter(name=quiz, quiz_owner=owner).first()
    if quiz is None:
        return JsonResponse({'error': 'Quiz does not exist'}, status=400)
    quiz.delete()
    return JsonResponse({'message': 'Quiz deleted'}, status=200)