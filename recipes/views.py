from django.db.models import Count
from rest_framework import generics, permissions, filters
from genshin_api.permissions import IsOwnerOrReadOnly
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeList(generics.ListAPIView):
    '''
        List recipes & create if logged in
    '''

    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        made_count=Count('made', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
        'made_count',
        'likes__created_at',
        'made__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
        Retrieve a recipe and edit or delete if you own it
    '''

    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recipe.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        made_count=Count('made', distinct=True),
    ).order_by('-created_at')
