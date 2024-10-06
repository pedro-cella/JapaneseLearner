from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hiragana", views.hiragana, name="hiragana"),
    path("katakana", views.katakana, name="katakana"),
]