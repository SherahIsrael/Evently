from django.test import TestCase
from eventure.models import eventsTable, usersTable


class TestModels(TestCase):

    def setUp(self):
        self.project1 = eventsTable.objects.create(
            name="eventsTable",
            budget=10000
        )
