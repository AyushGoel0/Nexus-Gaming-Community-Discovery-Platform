from django.contrib import admin
from .models import Community, CommunityMembership, Game, Genre, UserGame

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


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")
    search_fields = ("name", "description", "owner__username")
    list_filter = ("created_at",)


@admin.register(CommunityMembership)
class CommunityMembershipAdmin(admin.ModelAdmin):
    list_display = ("community", "user", "role", "joined_at")
    search_fields = ("community__name", "user__username")
    list_filter = ("role", "joined_at")


@admin.register(UserGame)
class UserGameAdmin(admin.ModelAdmin):
    list_display = ("user", "game", "status", "is_favorite", "updated_at")
    search_fields = ("user__username", "game__title")
    list_filter = ("status", "is_favorite")