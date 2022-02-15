from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import UserManager
from social.models import User
from social.apiSocial.serializers import UserSerializer
from social.forms import UserRegisterForm
from django.contrib.auth import authenticate


def all_user():
    user = User.objects.all()
    profile_serializer = UserSerializer(user, many=True)
    return profile_serializer.data


def save_user(save):
    user = User.objects.create_user(username=save['username'], email=save['email'], password=save['password'])
    user_serializer = UserSerializer(user)
    return user_serializer.data


def get_user(get):
    user = User.objects.filter(id=get).first()

    user_serializer = UserSerializer(user)
    return user_serializer.data


def get_user_username(get):
    user = User.objects.filter(username=get).first()
    user_serializer = UserSerializer(user)
    return user_serializer.data




def get_user_email(get):
    user = User.objects.filter(email=get).first()
    user_serializer = UserSerializer(user)
    return user_serializer.data


def update_user(update, update_object):
    user = User.objects.filter(user=update).first()
    user_serializer = UserSerializer(user, data=update_object)
    if user_serializer.is_valid():
        user_serializer.save()
        return user_serializer.data
    return user_serializer.errors


def authentication(data):
    print(data)
    user = authenticate(username=data['username'], password=data['password'])
    user_serializer = UserSerializer(user)
    if user is not None:
        return user_serializer.data
    else:
        return data
