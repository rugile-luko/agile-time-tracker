import datetime
from django.test import TestCase, tag
from tracker.templatetags.calculator_tags import duration


@tag('unit')
class CalculatorTagsTests(TestCase):
    def test_no_hours_no_minutes(self):
        self.assertEqual(duration(datetime.timedelta(hours=0, minutes=0)), "No Time Tracked")

    def test_no_hours(self):
        self.assertEqual(duration(datetime.timedelta(hours=0, minutes=20)), "20 min")

    def test_one_hour_and_minutes(self):
        self.assertEqual(duration(datetime.timedelta(hours=1, minutes=15)), "1 hour 15 min")

    def test_one_hour(self):
        self.assertEqual(duration(datetime.timedelta(hours=1)), "1 hour")

    def test_more_hours(self):
        self.assertEqual(duration(datetime.timedelta(hours=3)), "3 hours")

    def test_another_options(self):
        self.assertEqual(duration(datetime.timedelta(hours=5, minutes=10)), "5 hours 10 min")
