from datetime import date
from django.test import TestCase
from .models import Game, Genre

# Create your tests here.

class CoreViewsTests(TestCase):
    def test_home_page(self):
        response = self.client.get("/")
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Find your next game and your next community.")
        self.assertTemplateUsed(response, "core/index.html")

    def test_health_check(self):
        response = self.client.get("/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

class GameModelTests(TestCase):
    def test_game_string_representation(self):
        game = Game.objects.create(
            title="Hades",
            description="A roguelike action game.",
            release_date=date(2020, 9, 17),
        )

        self.assertEqual(str(game), "Hades")

    def test_games_are_ordered_by_title(self):
        Game.objects.create(title="Zelda")
        Game.objects.create(title="Apex Legends")

        self.assertEqual(
            list(Game.objects.values_list("title", flat=True)),
            ["Apex Legends", "Zelda"],
        )

class GameListViewTests(TestCase):
    def test_game_list_displays_games(self):
        game = Game.objects.create(
            title="Hades",
            description="A roguelike action game.",
        )
        genre = Genre.objects.create(name="Roguelike")
        game.genres.add(genre)

        response = self.client.get("/games/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hades")
        self.assertContains(response, "Roguelike")
        self.assertTemplateUsed(response, "core/game_list.html")

    def test_game_list_displays_empty_state(self):
        response = self.client.get("/games/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No games available yet.")

class GenreModelTests(TestCase):
    def test_genre_string_representation(self):
        genre = Genre.objects.create(name="RPG")

        self.assertEqual(str(genre), "RPG")

    def test_genre_names_are_unique(self):
        Genre.objects.create(name="RPG")

        with self.assertRaises(Exception):
            Genre.objects.create(name="RPG")

    def test_game_can_have_multiple_genres(self):
        game = Game.objects.create(title="Hades")
        action = Genre.objects.create(name="Action")
        roguelike = Genre.objects.create(name="Roguelike")

        game.genres.add(action, roguelike)

        self.assertEqual(game.genres.count(), 2)
        self.assertEqual(action.games.count(), 1)
        self.assertEqual(roguelike.games.count(), 1)
