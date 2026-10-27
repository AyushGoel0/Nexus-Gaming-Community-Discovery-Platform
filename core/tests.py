from django.test import TestCase

# Create your tests here.

class CoreViewsTests(TestCase):
    def test_home_page(self):
        response = self.client.get("/")
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Nexus")

    def test_health_check(self):
        response = self.client.get("/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})