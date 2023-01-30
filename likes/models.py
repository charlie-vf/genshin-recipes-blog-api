from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe


class Likes(models.Model):
    '''
    Like model for owner(User who likes) & recipe
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe, related_name='likes', on_delete=models.CASCADE
    )
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-liked_at']
        unique_together = ['owner', 'recipe']

    def __str__(self):
        return f'{self.owner} {self.recipe}'
