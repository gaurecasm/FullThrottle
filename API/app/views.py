from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import  api_settings
from rest_framework.permissions import  IsAuthenticatedOrReadOnly, IsAuthenticated

from app import models, serializers
from app import  permissions

from django.dispatch import  Signal
from django.contrib.auth import authenticate, user_logged_in
# Create your views here.


class UserProfileviewSet(viewsets.ModelViewSet):
    """handle creating and updating profile"""
    serializer_class = serializers.UserPforileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filters_backends = (filters.SearchFilter,)
    serach_fields = ('name')

class UserLoginApiView(ObtainAuthToken):
    """handle creating user login authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    # user_logged_in.send(sender=user.__class__, request=self.context['request'], user=user)