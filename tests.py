from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task


class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="test12345",
        )

    def test_create_task(self):
        task = Task.objects.create(
            user=self.user,
            title="Learn Django",
            description="Complete CRUD project",
            completed=False,
        )

        self.assertEqual(task.title, "Learn Django")
        self.assertFalse(task.completed)

    def test_string_representation(self):
        task = Task.objects.create(
            user=self.user,
            title="Sample Task",
        )

        self.assertEqual(str(task), "Sample Task")