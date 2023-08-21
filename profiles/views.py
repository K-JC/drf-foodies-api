from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):
    """
    Lists all the profiles
    """
    def get(self, request):
        profiles = Profile.objects.all()
        return Response(profiles)

    def get(self, request):
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
