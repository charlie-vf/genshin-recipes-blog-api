from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    '''
        Model for Recipes
    '''

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True)
    method = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../ei-miko-cooking_mkhllz', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
