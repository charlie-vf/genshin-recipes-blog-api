from django.shortcuts import render
from rest_framework import generics, permissions
from genshin_api.permissions import IsOwnerOrReadOnly
from .models import Likes
from .serializers import LikesSerializer


class LikesList(generics.ListCreateAPIView):
    '''
        View to create and list likes on recipes
    '''
    serializer_class = LikesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikesDetail(generics.RetrieveDestroyAPIView):
    '''
        Retrieve a like by id to allow unliking
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()
