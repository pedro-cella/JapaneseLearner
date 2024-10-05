from django.db import models

class Hiragana(models.Model):
    romaji = models.CharField(max_length=10)
    kana = models.CharField(max_length=10)
    
class Katakana(models.Model):
    romaji = models.CharField(max_length=10)
    kana = models.CharField(max_length=10)