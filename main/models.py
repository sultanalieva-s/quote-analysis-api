from django.db import models

# Create your models here.


class Quote(models.Model):
    quote = models.TextField(unique=True)


class QuoteAnalysis(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    total_letters = models.IntegerField()
    total_vowels = models.IntegerField()
    total_consonants = models.IntegerField()
    average_word_length = models.IntegerField()
    letter_repetitions = models.TextField()
    longest_words = models.TextField()
