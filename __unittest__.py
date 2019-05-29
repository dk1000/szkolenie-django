from dataclasses import dataclass
from datetime import date, datetime, timezone, timedelta
from typing import Optional
from unittest import TestCase

YEAR = 365.2425  # days

@dataclass
class Person:
    first_name: str
    last_name: str
    date_of_birth: Optional[date] = None

    def __post_init__(self):
        self.add_date = datetime.now(tz=timezone.utc)

        if self.date_of_birth:
            if not isinstance(self.date_of_birth, date):
                raise TypeError('Date of Birth must be Type[date]')

    def age(self) -> float:
        if not self.date_of_birth:
            return None

        age = datetime.now().date() - self.date_of_birth
        return round(age.days / YEAR)


class PersonTest(TestCase):
    def setUp(self) -> None:
        self.person = Person(first_name='Jan', last_name='Twardowski')

    def test_create_person(self):
        p = Person(first_name='Jan', last_name='Twardowski')
        self.assertEqual(p.first_name, 'Jan')
        self.assertEqual(p.last_name, 'Twardowski')

    def test_date_of_birth(self):
        today = date.today()
        p = Person(first_name='Jan', last_name='Twardowski', date_of_birth=today)
        self.assertEqual(p.date_of_birth, today)

    def test_created_date(self):
        now = datetime.now(tz=timezone.utc)
        p = Person(first_name='Jan', last_name='Twardowski')
        self.assertEqual(p.add_date.date(), now.date())     # check if date is the same
        self.assertEqual(p.add_date.tzinfo, timezone.utc)   # check if timezone is UTC
        self.assertEqual(p.add_date.time().hour, now.time().hour)
        self.assertEqual(p.add_date.time().minute, now.time().minute)
        self.assertEqual(p.add_date.time().second, now.time().second)

    def test_bad_name(self):
        p = Person(first_name='Jan', last_name='asdas%$^#$#sd a')
        self.assertRegex(p.last_name, r'\w+')

    def test_birth_date_bad_type(self):
        with self.assertRaises(TypeError):
            Person(first_name='Jan', last_name='Twardowski', date_of_birth='1970-01-01')

    def test_age(self):
        now = date.today() - timedelta(years=50)
        self.assertEqual(self.person.age(), 50)
