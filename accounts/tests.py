from django.test import TestCase
from django.urls import reverse

from .models import User


class UserModelTests(TestCase):
    def test_user_supports_profile_fields(self):
        user = User.objects.create_user(
            username="player1",
            password="Strong-pass-123",
            display_name="Player One",
            bio="Enjoys cooperative games.",
        )

        self.assertEqual(str(user), "player1")
        self.assertEqual(user.display_name, "Player One")
        self.assertEqual(user.bio, "Enjoys cooperative games.")


class AuthenticationViewTests(TestCase):
    def test_accounts_home_redirects_anonymous_users_to_login(self):
        response = self.client.get(reverse("accounts:home"))

        self.assertRedirects(response, reverse("accounts:login"))

    def test_authenticated_users_are_redirected_from_auth_pages(self):
        user = User.objects.create_user(
            username="player1",
            password="Strong-pass-123",
        )
        self.client.force_login(user)

        for route_name in ("accounts:home", "accounts:login", "accounts:register"):
            with self.subTest(route_name=route_name):
                response = self.client.get(reverse(route_name))
                self.assertRedirects(response, reverse("accounts:profile"))

    def test_registration_creates_user_and_redirects_to_login(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "newplayer",
                "email": "newplayer@example.com",
                "display_name": "New Player",
                "bio": "Likes RPGs.",
                "password1": "Strong-pass-123",
                "password2": "Strong-pass-123",
            },
        )

        self.assertRedirects(response, reverse("accounts:login"))
        user = User.objects.get(username="newplayer")
        self.assertEqual(user.display_name, "New Player")

    def test_registration_rejects_mismatched_passwords(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "newplayer",
                "password1": "Strong-pass-123",
                "password2": "Different-pass-123",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"].has_error("password2", "password_mismatch"))
        self.assertFalse(User.objects.filter(username="newplayer").exists())

    def test_login_and_logout(self):
        user = User.objects.create_user(
            username="player1",
            password="Strong-pass-123",
        )

        login_response = self.client.post(
            reverse("accounts:login"),
            {"username": user.username, "password": "Strong-pass-123"},
        )

        self.assertRedirects(login_response, reverse("accounts:profile"))
        self.assertTrue(self.client.session.get("_auth_user_id"))

        logout_response = self.client.post(reverse("accounts:logout"))

        self.assertRedirects(logout_response, reverse("accounts:login"))
        self.assertIsNone(self.client.session.get("_auth_user_id"))

    def test_profile_requires_authentication(self):
        response = self.client.get(reverse("accounts:profile"))

        self.assertRedirects(
            response,
            f"{reverse('accounts:login')}?next={reverse('accounts:profile')}",
        )

    def test_authenticated_user_can_update_profile(self):
        user = User.objects.create_user(
            username="player1",
            password="Strong-pass-123",
        )
        self.client.force_login(user)

        response = self.client.post(
            reverse("accounts:profile"),
            {
                "email": "player1@example.com",
                "display_name": "Updated Player",
                "bio": "Now plays strategy games.",
            },
        )

        self.assertRedirects(response, reverse("accounts:profile"))
        user.refresh_from_db()
        self.assertEqual(user.email, "player1@example.com")
        self.assertEqual(user.display_name, "Updated Player")
        self.assertEqual(user.bio, "Now plays strategy games.")
