from django.db import IntegrityError
from rest_framework import serializers
from .models import Made


class MadeSerializer(serializers.ModelSerializer):
    '''
        Serializer for Made model
    '''

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Made
        fields = [
            'id', 'made_at', 'owner', 'recipe'
        ]

    # Handles duplicates through unique constraint declared in model
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'details': 'possible duplicate like'
            })
