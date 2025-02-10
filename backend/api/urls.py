from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [

    #--------------Setting up db data / teste environment-----------------
    path('hello/', views.HelloWorld.as_view(), name='hello_world'),
    #path('japanese/', views.japanese, name="japanese"),
    #path('get-by-tag/<str:tag>', views.get_by_tag, name="get-by-tag"),
    path('debug', views.debug, name="debug"),
    path('alpha', views.load_alpha_test_data, name="alpha"),
    path('difficulty', views.create_difficulty, name="difficulty"),


    #--------------API--------------------------------

    path('get-csrf-token', views.get_csrf_token, name="get-csrf-token"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('get_user', views.get_user, name="get_user"),
    path('own-deck', views.QuizView.as_view(), name="own-deck"),
    path('profile/<str:username>', views.get_profile, name="profile"),
    path('add-follower', views.add_follower, name="add-follower"),

]
