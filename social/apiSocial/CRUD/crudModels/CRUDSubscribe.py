from social.models import Relationship
from .CRUDUser import get_user_username
from django.contrib.auth.models import User
from django.db import connection


def get_subscript(pk):
    user = get_user_username(pk)
    if user.get('id') is not None:
        cursor = connection.cursor()
        cursor.execute(
            "select social_relationship.to_user_id from social_relationship where social_relationship.from_user_id = %s",
            [user.get('id')])
        array_result = []
        array = ['id', 'username']
        for el in cursor.fetchall():
            dic = {}
            for data in el:
                dic[array[0]] = data
            dic[array[1]] = User.objects.filter(id=data).first().username
            array_result.append(dic)
        return array_result
    else:
        return {}


def set_subscribe(to, of_from):
    id_of_form = User.objects.filter(username=of_from).first()
    if_to = User.objects.filter(username=to).first()
    if id_of_form is not None and if_to is not None:
        subscribe = Relationship(to_user=if_to, from_user=id_of_form)
        subscribe.save()
        return get_subscript(of_from)
    else:
        return {}


def delete_subscribe(to, of_from):
    id_from = get_user_username(of_from).get('id')
    id_to = get_user_username(to).get('id')
    if id_from is not None and id_to is not None:
        subs = Relationship.objects.filter(from_user_id=id_from, to_user_id=id_to).first()
        subs.delete()
        return get_subscript(to)
    else:
        return {}


def get_subscript_user(pk):
    user = get_user_username(pk)
    if user.get('id') is not None:
        cursor = connection.cursor()
        cursor.execute(
            "select social_relationship.from_user_id from social_relationship where social_relationship.to_user_id = %s",
            [user.get('id')])
        array_result = []
        array = ['id', 'username']
        for el in cursor.fetchall():
            dic = {}
            for data in el:
                dic[array[0]] = data
            dic[array[1]] = User.objects.filter(id=data).first().username
            array_result.append(dic)
        return array_result
    else:
        return {}
