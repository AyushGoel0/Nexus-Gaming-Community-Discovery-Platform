from django.contrib import admin
from .models import Game, Genre

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date", "created_at")
    search_fields = ("title", "description")
    list_filter = ("genres",)