from django.shortcuts import render
from rest_framework import generics, permissions
from genshin_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowersList(generics.ListCreateAPIView):
    '''
        View to list all followers & create a follow
    '''
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowersDetail(generics.RetrieveDestroyAPIView):
    '''
        Retrieve follower detail
        Unfollow(delete) if owner of follow
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
