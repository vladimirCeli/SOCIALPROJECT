from social.apiSocial.serializers import PostSerializer
from django.contrib.auth.models import User
from social.models import Post, Profile
from django.db import connection


def all_post():
    cursor = connection.cursor()
    cursor.execute(
        "select social_profile.id, social.id, social.timestamp, social.content,auth_user.username from social_post as "
        "social inner join auth_user on social.user_id = auth_user.id inner join social_profile on auth_user.id = "
        "social_profile.user_id")
    result = cursor.fetchall()
    array = ['id_profile', 'id', 'timestamp', 'content', 'username']
    array_result = []

    for i in result:
        dic_r = {}
        for e, n in zip(i, array):
            dic_r[n] = e
        dic_r["image"] = Profile.objects.filter(id=dic_r[array[0]]).first().image.url
        array_result.append(dic_r)
    return array_result


def save_post(save):
    post = PostSerializer(data=save)
    if post.is_valid():
        post.save()
        print(post)
        return post.data
    return post.errors


def get_post(get):
    cursor = connection.cursor()
    cursor.execute(
        "select social_profile.id, social.id, social.timestamp, social.content,auth_user.username from social_post as "
        "social inner join auth_user on social.user_id = auth_user.id inner join social_profile on auth_user.id = "
        "social_profile.user_id where social.id = %s",
        [get])
    array = ['id_profile', 'id', 'timestamp', 'content', 'username']
    dict_post = {}
    for value, name in zip(cursor.fetchone(), array):
        dict_post[name] = value
    dict_post["image"] = Profile.objects.filter(id=dict_post[array[0]]).first().image.url
    return dict_post


def get_post_single_profile(get):
    cursor = connection.cursor()
    cursor.execute(
        "select social_profile.id, social.id, social.timestamp, social.content,auth_user.username from social_post as "
        "social inner join auth_user on social.user_id = auth_user.id inner join social_profile on auth_user.id = "
        "social_profile.user_id where auth_user.username = %s",
        [get])

    try:
        value = cursor.fetchall()
        array = ['id_profile', 'id', 'timestamp', 'content', 'username']
        array_result = []
        for i in value:
            dic_r = {}
            for e, n in zip(i, array):
                dic_r[n] = e
            dic_r["image"] = Profile.objects.filter(id=dic_r[array[0]]).first().image.url
            array_result.append(dic_r)
        return array_result
    except:
        return {}


def update_post(update, update_object):
    post = Post.objects.filter(user=update).first()
    print(update_object)
    post_serializer = PostSerializer(post, data=update_object)
    if post_serializer.is_valid():
        post_serializer.save()
        print(post_serializer.data)
        return post_serializer.data
    return post_serializer.errors


def delete_post(delete):
    post = Post.objects.filter(user=delete).first()
    post.delete()
    return 200
