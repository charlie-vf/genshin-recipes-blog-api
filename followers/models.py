from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    '''
        Follower model for owner(user following user) &
        followed(user followed by owner)
    '''

    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )

    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # unique ensures Owner cannot follow same user multiple times
        ordering = ['-followed_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
