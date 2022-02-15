from social.models import User
from django.contrib.auth.models import models


class UserAux:
    def __init__(self):
        self.username = None
        self.password = None
        self.email = None
        self.image = None

    def copy_user(self, user, profile):
        self.username = user.username
        self.email = user.email
        self.password = user.password
        self.image = profile.image
