from django.conf import settings
from django.db import models

# Create your models here.

#Genre model to represent different game genres
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

#Game model to represent individual games
class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField(
        Genre,
        related_name="games",
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title", "-release_date"]
        verbose_name = "Game"
        verbose_name_plural = "Games"
        
    def __str__(self) -> str:
        return self.title
