from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from genshin_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    '''
        List all profiles
    '''
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        recipes_count=Count('owner__recipe', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    # sort profiles by number of recipes, followers, following
    # sort profiles by date user followed profile & was followed
    # by another user
    ordering_fields = [
        'recipes_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at'
    ]

    filterset_fields = [
        # filter through profiles that are following a profile
        'owner__following__followed__profile',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    '''
        Retrieve or update a profile if you're the owner.
    '''
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        recipes_count=Count('owner__recipe', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
