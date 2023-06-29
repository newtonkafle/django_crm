from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Initialized the default user model with this model. """
    pass


class Lead(models.Model):
    """Lead model for the lead schema"""
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    """Agent model for the agent schema"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
