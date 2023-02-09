from django.db.models import Count
from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
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

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(
            recipes, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
        'made_count',
        'likes__created_at',
        'made__created_at',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    filterset_fields = [
        # user feed - posts by users they follow
        'owner__followed__owner__profile',
        # posts the user has liked
        'likes__owner__profile',
        # posts the user has marked as made
        'made__owner__profile',
        # user posts
        'owner__profile',
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
