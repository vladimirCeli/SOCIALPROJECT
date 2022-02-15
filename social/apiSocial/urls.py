from django.urls import path
from social.apiSocial.CRUD.restModels.RESTProfile import rest_profile, rest_single_profile, rest_get_profile
from social.apiSocial.CRUD.restModels.RESTUser import *
from social.apiSocial.CRUD.restModels.RESTPost import rest_post, rest_single_post, rest_get_singles_posts_profile
from social.apiSocial.CRUD.restModels.RESTSubscribe import get_all_subscribe_user, set_subscribe_user, \
    delete_subscribe_user, get_all_subscription_user

urlpatterns = [
    path('profiles/', rest_profile, name='profile_a;;'),
    path('profiles/<str:pk>', rest_get_profile, name='profile_uni'),
    path('users/', rest_user, name='user_all'),
    path('posts/', rest_post, name='posts_all'),
    # single result API
    path('profiles/<int:pk>', rest_single_profile, name='single_profile'),
    path('users/id/<int:pk>', rest_single_user, name='single_user'),
    path('users/username/<str:pk>', rest_single_user_username, name='single_user'),
    path('users/email/<str:pk>', rest_single_user_email, name='single_user_email'),
    path('posts/<int:pk>', rest_single_post, name='single_posts'),
    path('posts/profile/<str:pk>', rest_get_singles_posts_profile, name='all_posts_profile'),
    # single authenticate
    path('users/auth/', rest_auth_username, name='auth'),

    # subscribe
    path('subscribe/<str:pk>', get_all_subscribe_user, name='subscribe'),
    path('subscribe/subscription/<str:pk>', get_all_subscription_user, name='subscribe'),
    path('subscribe/set/<str:to>/<str:of_from>', set_subscribe_user, name='subscribe_set'),
    path('subscribe/delete/<str:to>/<str:of_from>', delete_subscribe_user, name='subscribe_delete')

]
