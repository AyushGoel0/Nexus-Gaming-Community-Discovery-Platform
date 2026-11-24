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

class Community(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_communities",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class CommunityMembership(models.Model):
    class Role(models.TextChoices):
        OWNER = "owner", "Owner"
        MODERATOR = "moderator", "Moderator"
        MEMBER = "member", "Member"

    community = models.ForeignKey(
        Community,
        on_delete=models.CASCADE,
        related_name="memberships",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="community_memberships",
    )
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.MEMBER,
    )
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["community", "user"],
                name="unique_community_membership",
            ),
        ]
        ordering = ["joined_at"]

    def __str__(self) -> str:
        return f"{self.user} - {self.community}"


class UserGame(models.Model):
    class Status(models.TextChoices):
        WANT_TO_PLAY = "want_to_play", "Want to play"
        PLAYING = "playing", "Playing"
        COMPLETED = "completed", "Completed"
        DROPPED = "dropped", "Dropped"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="game_library",
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="player_entries",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.WANT_TO_PLAY,
    )
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "game"],
                name="unique_user_game_entry",
            ),
        ]
        ordering = ["-updated_at"]

    def __str__(self) -> str:
        return f"{self.user} - {self.game}"
