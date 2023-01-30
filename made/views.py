from django.shortcuts import render
from rest_framework import generics, permissions
from genshin_api.permissions import IsOwnerOrReadOnly
from .models import Made
from .serializers import MadeSerializer


class MadeList(generics.ListCreateAPIView):
    '''
        View to add a 'made' count & list number
        of times recipes has been made by users
    '''
    serializer_class = MadeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Made.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MadeDetail(generics.RetrieveDestroyAPIView):
    '''
        Retrieve a 'made' instance by id to remove
        e.g. if clicked by accident
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MadeSerializer
    queryset = Made.objects.all()
