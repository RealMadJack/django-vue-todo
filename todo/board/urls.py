from django.urls import path

from .apps import BoardConfig
from .views import index_view

app_name = BoardConfig.name

urlpatterns = [
    path("", index_view, name='index')
]
