from django.test import TestCase
from django.urls import resolve


class BoardUrlsTest(TestCase):
    def setUp(self):
        self.resolve_api_index = resolve('/api/')
        self.resolve_api_list = resolve('/api/article/')
        self.resolve_api_obj = resolve('/api/article/1/')

    def test_api_root(self):
        self.assertEqual(self.resolve_api_index.view_name, 'board:api-root')

    def test_api_article_list(self):
        self.assertEqual(self.resolve_api_list.view_name, 'board:article-list')

    def test_api_article_obj(self):
        self.assertEqual(self.resolve_api_obj.view_name, 'board:article-detail')
