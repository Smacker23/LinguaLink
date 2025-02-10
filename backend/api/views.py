from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.middleware.csrf import get_token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from quiz.models import Question, Tag, Quiz, Difficulty
from user.models import Profile, Admin
from user.views import create_user, login_user, logout_user, auth_token, load_profile_data, follow_user, get_user_by_token
from quiz.views import create_quiz, get_quiz, get_quizes
def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

class HelloWorld(APIView):
    def get(self, request):
        print(request.session)
        print(request.session.get('username')) 
        print(request.user)
        print(request.user.is_authenticated)
        return Response({"message": "Hello, world!"})

""" def serialize_words_list(tag):
    words = Word.objects.filter(tags__tag=tag)
    serializer = WordSerializer(words, many=True)
    return serializer.data

def create_alphabet(tag_name, alphabet):
    tag = Tag.objects.create(tags__tag=tag_name)
    for word, translated in alphabet.items():
            word = Word.objects.create(word=word, translated=translated)
            word.tags.add(tag)


def japanese(request):
    HIRAGANA = {'Ã£ÂÂ': 'a', 'Ã£ÂÂ': 'i', 'Ã£ÂÂ': 'u', 'Ã£ÂÂ': 'e', 'Ã£ÂÂ': 'o',
                'Ã£ÂÂ': 'ka', 'Ã£ÂÂ': 'ki', 'Ã£ÂÂ': 'ku', 'Ã£ÂÂ': 'ke', 'Ã£ÂÂ': 'ko',
                'Ã£ÂÂ': 'sa', 'Ã£ÂÂ': 'shi', 'Ã£ÂÂ': 'su', 'Ã£ÂÂ': 'se', 'Ã£ÂÂ': 'so',
                'Ã£ÂÂ': 'ta', 'Ã£ÂÂ¡': 'tchi', 'Ã£ÂÂ¤': 'tsu', 'Ã£ÂÂ¦': 'te', 'Ã£ÂÂ¨': 'to',
                'Ã£ÂÂª': 'na', 'Ã£ÂÂ«': 'ni', 'Ã£ÂÂ¬': 'nu', 'Ã£ÂÂ­': 'ne', 'Ã£ÂÂ®': 'no',
                'Ã£ÂÂ¯': 'ha', 'Ã£ÂÂ²': 'hi', 'Ã£ÂÂµ': 'fu', 'Ã£ÂÂ¸': 'he', 'Ã£ÂÂ»': 'ho',
                'Ã£ÂÂ¾': 'ma', 'Ã£ÂÂ¿': 'mi', 'Ã£ÂÂ': 'mu', 'Ã£ÂÂ': 'me', 'Ã£ÂÂ': 'mo',
                'Ã£ÂÂ': 'ya', 'Ã£ÂÂ': 'yu', 'Ã£ÂÂ': 'yo',
                'Ã£ÂÂ': 'ra', 'Ã£ÂÂ': 'ri', 'Ã£ÂÂ': 'ru', 'Ã£ÂÂ': 're', 'Ã£ÂÂ': 'ro',
                'Ã£ÂÂ': 'wa', 'Ã£ÂÂ': 'wo',
                'Ã£ÂÂ': 'n',
                'Ã£ÂÂ': 'ga', 'Ã£ÂÂ': 'gi', 'Ã£ÂÂ': 'gu', 'Ã£ÂÂ': 'ge', 'Ã£ÂÂ': 'go',
                'Ã£ÂÂ': 'za', 'Ã£ÂÂ': 'ji', 'Ã£ÂÂ': 'zu', 'Ã£ÂÂ': 'ze', 'Ã£ÂÂ': 'zo',
                'Ã£ÂÂ ': 'da', 'Ã£ÂÂ¢': 'dji', 'Ã£ÂÂ¥': 'du', 'Ã£ÂÂ§': 'de', 'Ã£ÂÂ©': 'do',
                'Ã£ÂÂ°': 'ba', 'Ã£ÂÂ³': 'bi', 'Ã£ÂÂ¶': 'bu', 'Ã£ÂÂ¹': 'be', 'Ã£ÂÂ¼': 'bo',
                'Ã£ÂÂ±': 'pa', 'Ã£ÂÂ´': 'pi', 'Ã£ÂÂ·': 'pu', 'Ã£ÂÂº': 'pe', 'Ã£ÂÂ½': 'po',}

    KATAKANA = {'Ã£ÂÂ¢': 'a', 'Ã£ÂÂ¤': 'i', 'Ã£ÂÂ¦': 'u', 'Ã£ÂÂ¨': 'e', 'Ã£ÂÂª': 'o',
                'Ã£ÂÂ«': 'ka', 'Ã£ÂÂ­': 'ki', 'Ã£ÂÂ¯': 'ku', 'Ã£ÂÂ±': 'ke', 'Ã£ÂÂ³': 'ko',
                'Ã£ÂÂµ': 'sa', 'Ã£ÂÂ·': 'shi', 'Ã£ÂÂ¹': 'su', 'Ã£ÂÂ»': 'se', 'Ã£ÂÂ½': 'so',
                'Ã£ÂÂ¿': 'ta', 'Ã£ÂÂ': 'tchi', 'Ã£ÂÂ': 'tsu', 'Ã£ÂÂ': 'te', 'Ã£ÂÂ': 'to',
                'Ã£ÂÂ': 'na', 'Ã£ÂÂ': 'ni', 'Ã£ÂÂ': 'nu', 'Ã£ÂÂ': 'ne', 'Ã£ÂÂ': 'no',
                'Ã£ÂÂ': 'ha', 'Ã£ÂÂ': 'hi', 'Ã£ÂÂ': 'fu', 'Ã£ÂÂ': 'he', 'Ã£ÂÂ': 'ho',
                'Ã£ÂÂ': 'ma', 'Ã£ÂÂ': 'mi', 'Ã£ÂÂ ': 'mu', 'Ã£ÂÂ¡': 'me', 'Ã£ÂÂ¢': 'mo',
                'Ã£ÂÂ¤': 'ya', 'Ã£ÂÂ¦': 'yu', 'Ã£ÂÂ¨': 'yo',
                'Ã£ÂÂ©': 'ra', 'Ã£ÂÂª': 'ri', 'Ã£ÂÂ«': 'ru', 'Ã£ÂÂ¬': 're', 'Ã£ÂÂ­': 'ro',
                'Ã£ÂÂ¯': 'wa', 'Ã£ÂÂ²': 'wo',
                'Ã£ÂÂ³': 'n',
                'Ã£ÂÂ¬': 'ga', 'Ã£ÂÂ®': 'gi', 'Ã£ÂÂ°': 'gu', 'Ã£ÂÂ²': 'ge', 'Ã£ÂÂ´': 'go',
                'Ã£ÂÂ¶': 'za', 'Ã£ÂÂ¸': 'ji', 'Ã£ÂÂº': 'zu', 'Ã£ÂÂ¼': 'ze', 'Ã£ÂÂ¾': 'zo',
                'Ã£ÂÂ': 'da', 'Ã£ÂÂ': 'dji', 'Ã£ÂÂ': 'du', 'Ã£ÂÂ': 'de', 'Ã£ÂÂ': 'do',
                'Ã£ÂÂ': 'ba', 'Ã£ÂÂ': 'bi', 'Ã£ÂÂ': 'bu', 'Ã£ÂÂ': 'be', 'Ã£ÂÂ': 'bo',
                'Ã£ÂÂ': 'pa', 'Ã£ÂÂ': 'pi', 'Ã£ÂÂ': 'pu', 'Ã£ÂÂ': 'pe', 'Ã£ÂÂ': 'po',}
    #word_count = Word.objects.filter(tags__tag="Hiragana").count()
    #if not hiragana_tag or word_count != HIRAGANA_LETTERS:
    if not Tag.objects.filter(tag="Hiragana").first():
        create_alphabet("Hiragana", HIRAGANA)
    if not Tag.objects.filter(tag="Katakana").first():
        create_alphabet("Katakana", KATAKANA)    
    hiragana_serializer = serialize_words_list("Hiragana")
    katakana_serializer = serialize_words_list("Katakana")
    return JsonResponse({'hiragana': hiragana_serializer, 'katakana': katakana_serializer}, safe=False)

def get_by_tag(request, tag):
     serializer = serialize_words_list(tag)
     return JsonResponse({'data': serializer}) """
    

def load_quiz():
    
    question_tag = Tag.objects.get_or_create(name="Character")
    quiz_tag = Tag.objects.get_or_create(name="Hiragana")
    admin = Admin.objects.get(name="test")
    HIRAGANA = {'Ã£ÂÂ': 'a', 'Ã£ÂÂ': 'i', 'Ã£ÂÂ': 'u', 'Ã£ÂÂ': 'e', 'Ã£ÂÂ': 'o',
                'Ã£ÂÂ': 'ka', 'Ã£ÂÂ': 'ki', 'Ã£ÂÂ': 'ku', 'Ã£ÂÂ': 'ke', 'Ã£ÂÂ': 'ko',
                'Ã£ÂÂ': 'sa', 'Ã£ÂÂ': 'shi', 'Ã£ÂÂ': 'su', 'Ã£ÂÂ': 'se', 'Ã£ÂÂ': 'so',
                'Ã£ÂÂ': 'ta', 'Ã£ÂÂ¡': 'tchi', 'Ã£ÂÂ¤': 'tsu', 'Ã£ÂÂ¦': 'te', 'Ã£ÂÂ¨': 'to',
                'Ã£ÂÂª': 'na', 'Ã£ÂÂ«': 'ni', 'Ã£ÂÂ¬': 'nu', 'Ã£ÂÂ­': 'ne', 'Ã£ÂÂ®': 'no',
                'Ã£ÂÂ¯': 'ha', 'Ã£ÂÂ²': 'hi', 'Ã£ÂÂµ': 'fu', 'Ã£ÂÂ¸': 'he', 'Ã£ÂÂ»': 'ho',
                'Ã£ÂÂ¾': 'ma', 'Ã£ÂÂ¿': 'mi', 'Ã£ÂÂ': 'mu', 'Ã£ÂÂ': 'me', 'Ã£ÂÂ': 'mo',
                'Ã£ÂÂ': 'ya', 'Ã£ÂÂ': 'yu', 'Ã£ÂÂ': 'yo',
                'Ã£ÂÂ': 'ra', 'Ã£ÂÂ': 'ri', 'Ã£ÂÂ': 'ru', 'Ã£ÂÂ': 're', 'Ã£ÂÂ': 'ro',
                'Ã£ÂÂ': 'wa', 'Ã£ÂÂ': 'wo',
                'Ã£ÂÂ': 'n',
                'Ã£ÂÂ': 'ga', 'Ã£ÂÂ': 'gi', 'Ã£ÂÂ': 'gu', 'Ã£ÂÂ': 'ge', 'Ã£ÂÂ': 'go',
                'Ã£ÂÂ': 'za', 'Ã£ÂÂ': 'ji', 'Ã£ÂÂ': 'zu', 'Ã£ÂÂ': 'ze', 'Ã£ÂÂ': 'zo',
                'Ã£ÂÂ ': 'da', 'Ã£ÂÂ¢': 'dji', 'Ã£ÂÂ¥': 'du', 'Ã£ÂÂ§': 'de', 'Ã£ÂÂ©': 'do',
                'Ã£ÂÂ°': 'ba', 'Ã£ÂÂ³': 'bi', 'Ã£ÂÂ¶': 'bu', 'Ã£ÂÂ¹': 'be', 'Ã£ÂÂ¼': 'bo',
                'Ã£ÂÂ±': 'pa', 'Ã£ÂÂ´': 'pi', 'Ã£ÂÂ·': 'pu', 'Ã£ÂÂº': 'pe', 'Ã£ÂÂ½': 'po',}
    difficulty = Difficulty.objects.get(name="Easy")
    for hiragana, latin in HIRAGANA.items():
        character = Question.objects.get_or_create(question=hiragana, answer=latin, difficulty=difficulty, question_owner=admin, reverse_question=True)
        if character[1]: character[0].tags.add(question_tag[0])
    quiz = Quiz.objects.get_or_create(name="Hiragana alphabet", difficulty=difficulty, public=True, quiz_owner=admin)
    if quiz[1]: quiz[0].tags.add(quiz_tag[0])
    if quiz[1]:quiz[0].questions.add(character)
def load_difficulty():
    DIFFICULTY = ["Easy", "Medium", "Hard"]
    for difficulty in DIFFICULTY:
        Difficulty.objects.get_or_create(name=difficulty)

def load_test_user():
    Admin.objects.get_or_create(name="test", email="test@test.com", password="test")

def load_alpha_test_data(requests):
    """
    Used only for testing purposes (Adds test data to database)
    """
    load_test_user()
    load_difficulty()
    load_quiz()
    return JsonResponse({"message": "Success!"})
def debug(request):
    user = Admin.objects.get_or_create(name="test", email="test", password="test")
    tag = Tag.objects.get_or_create(name="test", difficulty="Easy")

    return JsonResponse({"message": "Hello, world!"})


def create_difficulty(request):
    load_difficulty()
    return JsonResponse({"message": "Success!"})




#-----------------User login------------------

@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    first_name = request.data.get('firstName').capitalize()
    last_name = request.data.get('lastName').capitalize()
    email = request.data.get('email')
    password = request.data.get('password')
    confirm_password = request.data.get('confirmPassword')
    rememberMe = request.data.get('rememberMe')
    return create_user(username, first_name, last_name, email, password, confirm_password, rememberMe)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    rememberMe = request.data.get('rememberMe')
    return login_user(username, password, rememberMe)

@api_view(['GET'])
def logout(request):
    return logout_user(request)

@api_view(['GET'])
def get_user(request):
    try:
        token = request.COOKIES.get('auth_token')
        user = get_user_by_token(token)
        user_data = {'username': user.username, 'email': user.email, 'first_name': user.first_name, 'name': user.last_name}
        return JsonResponse({'isAuthenticated': True, 'user': user_data}, status=200)
    except:
       return JsonResponse({'isAuthenticated': False, 'user': ''}, status=200)
    





#----------------Decks------------------


class QuizView(APIView):
    """
    Quiz json file structure:
    {
    "quiz": {
        "name": "Sample Quiz",
        "difficulty": "Easy",
        "tags": ["General Knowledge", "Fun"],
        "questions": [
            {
                "question": "Question 1",
                "answer": "Answer 1",
                "difficulty": "Easy",
                "tags": ["Tag 1", "Tag 2", "Tag 3"]
            },
            {
                "question": "Question 2",
                "answer": "Answer 2",
                "difficulty": "Medium",
                "tags": ["Tag 4", "Tag 5"]
            }
        ]
    }
}

    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        owner = Profile.objects.get(email=request.user.email)
        quiz = request.GET.get('name')
        return get_quizes(owner, quiz)
    
    def post(self, request):
        owner = Profile.objects.get(email=request.user.email)
        quiz = request.data['quiz']
        return create_quiz(owner, quiz)
    



#-----------------Profile------------------


def get_profile(request):
    token = request.COOKIES.get('auth_token')
    user = get_user_by_token(token)
    return load_profile_data(user)

@api_view(['POST'])
def add_follower(request):
    token = request.COOKIES.get('auth_token')
    user = get_user_by_token(token)
    to_follow = request.data['username']
    print("here")
    to_follow = Profile.objects.filter(username_lowercase=to_follow.lower()).first()
    return follow_user(user, to_follow)


@api_view(['GET'])
def get_profile(request, username):
    print(username)
    token = request.COOKIES.get('auth_token')
    user = get_user_by_token(token)
    profile = Profile.objects.filter(username_lowercase=username.lower()).first()    
    if profile is None:
        return JsonResponse({'error': 'User does not exist'}, status=400)
    return load_profile_data(profile, user == profile)