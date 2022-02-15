from rest_framework.views import  APIView
from rest_framework.response import Response
from social.models import Profile
from social.apiSocial.serializers import ProfileSerializer


class CRUDProfile(APIView):
    def get(self, request):
        profile = Profile.objects.all()
        profile_serializer = ProfileSerializer(profile, many=True)
        return Response(profile_serializer.data)
