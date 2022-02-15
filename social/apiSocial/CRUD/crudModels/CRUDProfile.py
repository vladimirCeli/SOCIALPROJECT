from social.apiSocial.serializers import ProfileSerializer
from social.models import Profile, User, Post
from django.db import connection


def all_profile():
    profile = Profile.objects.all()
    profile_serializer = ProfileSerializer(profile, many=True)
    return profile_serializer.data


def save_profile(save):
    new_profile = ProfileSerializer(data=save)
    if new_profile.is_valid():
        new_profile.save()
        return new_profile
    return new_profile.errors


def get_profile(get):
    profile = Profile.objects.filter(id=get).first()
    profile_serializer = ProfileSerializer(profile)
    return profile_serializer.data


def update_profile(update, update_object):
    profile = Profile.objects.filter(user=update).first()
    profile_serializer = ProfileSerializer(profile, data=update_object)
    if profile_serializer.is_valid():
        profile_serializer.save()
        return profile_serializer.data
    return profile_serializer.errors


def delete_profile(delete):
    profile = Profile.objects.filter(user=delete).first()
    profile.delete()
    return 200


def get_profile_username(username):
    cursor = connection.cursor()

    cursor.execute(
        "select social_profile.id, social.id, social.timestamp,auth_user.email ,auth_user.username from social_post as "
        "social inner join auth_user on social.user_id = auth_user.id inner join social_profile on auth_user.id = "
        "social_profile.user_id where auth_user.username = %s",
        [username])
    #   try:
    value = cursor.fetchone()
    array = [' id_profile', 'id', 'timestamp', 'email', 'username']
    data = User.objects.filter(username=username).first()
    profile = Profile.objects.filter(user_id=data.id).first()
    post = Post.objects.filter(user_id=profile.id).first()
    dic_r = {
        'id_profile': data.id, 'is': profile.id,
        'email': data.email,
        'username': data.username, 'image': profile.image.url
    }
    if post is not None:
        dic_r['timestamp'] = post.timestamp
    return dic_r
