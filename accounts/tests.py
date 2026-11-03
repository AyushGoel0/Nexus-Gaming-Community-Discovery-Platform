from django.test import TestCase

from .models import User


class UserModelTests(TestCase):
    def test_user_supports_profile_fields(self):
        user = User.objects.create_user(
            username="player1",
            password="secure-password",
            display_name="Player One",
            bio="Enjoys cooperative games.",
        )

        self.assertEqual(str(user), "player1")
        self.assertEqual(user.display_name, "Player One")
        self.assertEqual(user.bio, "Enjoys cooperative games.")
