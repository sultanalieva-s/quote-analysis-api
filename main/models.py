from django.db import models

# Create your models here.


class QuoteAnalysis(models.Model):
    total_letters = models.IntegerField()
    total_vowels = models.IntegerField()
    total_consonants = models.IntegerField()
    average_word_length = models.IntegerField()
    letter_repetitions = models.TextField()
    longest_words = models.TextField()


class Quote(models.Model):
    quote = models.TextField(unique=True)
    analysis = models.ForeignKey(QuoteAnalysis, on_delete=models.CASCADE)
