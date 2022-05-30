from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from todolist.models import Task


class TaskTests(APITestCase):
    def setUp(self):
        self.user = User(email="foo@bar.com", username="test")
        self.password = "some_password"
        self.user.set_password(self.password)
        self.user.save()

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        """Ensure we can create a new task"""
        url = "/task/"
        data = {
            "owner": self.user.id,
            "title": "Tests1",
            "description": "test description",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(response.data["title"], data["title"])
