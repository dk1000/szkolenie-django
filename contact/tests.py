from datetime import date, timedelta
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from contact.models import Person


class PersonTest(TestCase):

    @classmethod
    def setUpClass(cls: TestCase) -> None:
        super().setUpClass()
        cls.ADMIN = User.objects.create(username='test', password='test')

    def setUp(self) -> None:
        self.person = Person.objects.create(
            first_name='Jan',
            last_name='Twardowski',
            date_of_birth=date.today(),
            add_author=self.ADMIN,
            modified_author=self.ADMIN)

    def test_create_person(self) -> None:
        self.assertEqual(self.person.first_name, 'Jan')
        self.assertEqual(self.person.last_name, 'Twardowski')

    def test_age(self) -> None:
        self.assertEqual(self.person.age(), 0)
        offset = 50 * settings.YEAR
        self.person.date_of_birth = date.today() - timedelta(days=offset)
        self.assertEqual(self.person.age(), 50)
