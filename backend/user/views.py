from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import Profile
import re
from user.serializer import ProfileSerializer
# Create your views here.

def get_user_by_token(token):
    token = Token.objects.get(key=token)
    user = token.user
    user = Profile.objects.filter(username=user.username).first()
    return user

def auth_token(response, token, remember_me=False):
    max_age = 30 * 24 * 60 * 60 if remember_me else None  # 30 days if Remember Me, otherwise session cookie
    response.set_cookie(
        key="auth_token",
        value=token,
        httponly=True,
        samesite="None",
        secure=True,
        max_age=max_age,
    )
    return response

def delete_cookie(self, key):
        """
        Default delete_cookie wasn't working, so i had to make my own.
        """
        self.set_cookie(
            key,
            max_age=0,
            secure=True,
            expires="Thu, 01 Jan 1970 00:00:00 GMT",
            samesite="None",
        )



def password_verification(error, password, confrim_password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if not re.match(pattern, password):
        error['password'] = 'Weak password! Must be 8+ chars with uppercase, lowercase, digit & special character.'
    elif password != confrim_password:
        error['confirmPassword'] = 'Passwords do not match'

def username_verification(error, username):
    pattern = r"^[\w]+$" 
    if not re.match(pattern, username):
        error['username'] = 'Invalid username. Cannot contain special characters'
    elif Profile.objects.filter(username_lowercase=username).exists():
        error['username'] = 'This username already exists'

def name_verification(error, first_name, last_name):
    pattern = r"^[A-Za-z\u00C0-\u017F\u0600-\u06FF\u0400-\u04FF\u4E00-\u9FFF\s]+$"  
    if not re.match(pattern, first_name):
        error['firstName'] = 'Invalid first name. Cannot contain special characters'
    if not re.match(pattern, last_name):
        error['lastName'] = 'Invalid last name. Cannot contain special characters'
        

def email_verification(error, email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, email):
        error['email'] = 'Invalid email'
    elif Profile.objects.filter(email=email).exists():
        error['email'] = 'This email already exists'

def create_user(username, first_name, last_name, email, password, confirm_password, rememberMe):
    username_lower = username.lower()
    error = {}
    username_verification(error, username_lower)
    name_verification(error, first_name, last_name)
    email_verification(error, email)
    password_verification(error, password, confirm_password)
    password = make_password(password)
    if error:
        return JsonResponse({'error': error}, status=400)
    Profile.objects.create(username=username, username_lowercase=username_lower, first_name=first_name, last_name=last_name, email=email, password=password)
    #auth_token
    token = Token.objects.create(user=Profile.objects.get(email=email))
    response = JsonResponse({'message': 'User created'}, status=200)
    response = auth_token(response, token.key, rememberMe)   

    return response


def login_user(username, password, rememberMe):
    username = username.lower()
    print(username, password, rememberMe)
    user = Profile.objects.filter(username_lowercase=username).first()
    if user is None:
        print("ha")
        return JsonResponse({'error': 'Usernme and password do not match'}, status=400)
    if user and check_password(password, user.password):
        token, _ = Token.objects.get_or_create(user=user)
        user = ProfileSerializer(user).data
        response = JsonResponse({'message': 'User logged in', 'user': user}, status=200)
        response = auth_token(response, token.key, rememberMe)   
        return response
    return JsonResponse({'error': 'Usernme and password do not match'}, status=400)

def logout_user(request):
    response = JsonResponse({"message": "Logged out successfully"}, status=200)
    delete_cookie(response, "auth_token")
    print(response.cookies)
    return response  


def load_profile_data(user, owner=False):
    username = user.username
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    followers = user.followers.all().count()
    following = user.following.all().count()
    return JsonResponse({'username': username, 'firstName': first_name, 'lastName': last_name, 'email': email, 'followers': followers, 'following': following, 'owner': owner}, status=200)

def load_followers_list(user):
    followers = user.followers.all().values('username')
    return JsonResponse({'followers': followers}, status=200)

def load_following_list(user):
    followers = user.following.all().values('username')
    return JsonResponse({'followers': followers}, status=200)


def follow_user(user, to_follow):
    print("ha")
    if to_follow is None:
        return JsonResponse({'error': 'User not found'}, status=400)
    user.following.add(to_follow)
    to_follow.followers.add(user)
    return JsonResponse({'message': 'User followed'}, status=200)
