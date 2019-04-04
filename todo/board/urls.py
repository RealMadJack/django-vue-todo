from django.urls import path
from rest_framework import routers

from .apps import BoardConfig
from .views import ArticleViewSet

app_name = BoardConfig.name


router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)

urlpatterns = [
] + router.urls
