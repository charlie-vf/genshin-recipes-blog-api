from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe


class Made(models.Model):
    '''
        Made model for recipes tried by users
    '''

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe, related_name='made', on_delete=models.CASCADE
    )
    made_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-made_at']
        unique_together = ['owner', 'recipe']

    def __str__(self):
        return f'{self.owner} {self.recipe}'
