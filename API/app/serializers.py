from rest_framework import  serializers
from app import models

class UserPforileSerializer(serializers.ModelSerializer):
    """serializer a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'location',
        
         'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name = validated_data['name'],
            location=validated_data['location'],
            password=validated_data['password']

        )
        return user
