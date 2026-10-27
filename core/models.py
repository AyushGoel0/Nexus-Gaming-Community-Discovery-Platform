from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title", "release_date"]
        verbose_name = "Game"
        verbose_name_plural = "Games"
        
    def __str__(self) -> str:
        return self.title