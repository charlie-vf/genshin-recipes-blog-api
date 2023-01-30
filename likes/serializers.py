from rest_framework import serializers
from .models import Likes


class LikesSerializer(serializers.ModelSerializer):
    '''
        Serializer for Likes model
    '''

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Likes
        fields = [
            'id', 'liked_at', 'owner', 'recipe'
        ]
