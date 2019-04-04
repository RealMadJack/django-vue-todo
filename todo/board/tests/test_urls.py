from django.test import TestCase
from django.urls import resolve


class BoardUrlsTest(TestCase):
    def setUp(self):
        self.resolve_index = resolve('/')

    def test_index(self):
        self.assertEqual(self.resolve_index.view_name, 'board:index')
