from django.test import TestCase, Client
from main.quote_analysis import *

client = Client()

# Create your tests here.


class QuoteAnalysisTestCases(TestCase):

    def setUp(self) -> None:
        self.string_1 = 'Ararat'
        self.string_2 = '   Ararat   '
        self.string_3 = 'Ar  ar  at'
        self.string_4 = '   Ar   ar   at   '
        self.string_5 = 'ArAraT'
        self.string_6 = 'Ararat ! %& ?'
        self.string_7 = 'Ararat 1234567890'
        self.string_8 = 'aAaAaA'
        self.string_9 = 'kKkKkK'
        self.string_10 = 'People say it\'s enough and I got my point across ...\
                            the point isn\'t across until we cross the point'
        self.string_11 = 'one two threee'
        self.empty_string = ''
        self.string_without_letters = '!@#$%^&*'
        self.string_12 = '1 12 123 1234 12345 123456 1234567 12345678'
        self.string_13 = 'same same same'
        self.string_14 = 'same same'
        self.string_15 = 'same'

    def test_count_letters(self):
        self.assertEqual(count_total_vowels_consonants(self.string_1)['total_letters'], 6)
        self.assertEqual(count_total_vowels_consonants(self.string_2)['total_letters'], 6)
        self.assertEqual(count_total_vowels_consonants(self.string_3)['total_letters'], 6)
        self.assertEqual(count_total_vowels_consonants(self.string_4)['total_letters'], 6)
        self.assertEqual(count_total_vowels_consonants(self.string_5)['total_letters'], 6)
        self.assertEqual(count_total_vowels_consonants(self.string_6)['total_letters'], 6)
        self.assertEqual(count_total_vowels_consonants(self.string_7)['total_letters'], 6)
        self.assertNotEqual(count_total_vowels_consonants(self.string_1)['total_letters'], 7)
        self.assertEqual(count_total_vowels_consonants(self.empty_string)['total_letters'], 0)

    def test_count_vowels(self):
        self.assertEqual(count_total_vowels_consonants(self.string_1)['total_vowels'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_2)['total_vowels'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_3)['total_vowels'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_4)['total_vowels'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_5)['total_vowels'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_6)['total_vowels'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_7)['total_vowels'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_8)['total_vowels'], 6)
        self.assertNotEqual(count_total_vowels_consonants(self.string_1)['total_vowels'], 5)
        self.assertEqual(count_total_vowels_consonants(self.empty_string)['total_vowels'], 0)

    def test_count_consonants(self):
        self.assertEqual(count_total_vowels_consonants(self.string_1)['total_consonants'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_2)['total_consonants'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_3)['total_consonants'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_4)['total_consonants'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_5)['total_consonants'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_6)['total_consonants'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_7)['total_consonants'], 3)
        self.assertEqual(count_total_vowels_consonants(self.string_9)['total_consonants'], 6)
        self.assertNotEqual(count_total_vowels_consonants(self.string_1)['total_consonants'], 5)
        self.assertEqual(count_total_vowels_consonants(self.empty_string)['total_consonants'], 0)

    def test_count_average_word_length(self):
        self.assertEqual(count_average_word_length(self.string_10), 4)
        self.assertEqual(count_average_word_length(self.string_11), 4)
        self.assertNotEqual(count_average_word_length(self.string_11), 5)
        self.assertEqual(count_average_word_length(self.empty_string), 0)
        self.assertEqual(count_average_word_length(self.string_without_letters), 0)

    def test_get_longest_words(self):
        self.assertEqual(get_longest_words(self.string_12), '12345678 1234567 123456')
        self.assertNotEqual(get_longest_words(self.string_12), '1234567 123456 12345678')
        # TODO: ask is words should be unique
        self.assertEqual(get_longest_words(self.string_13), 'same same same')
        self.assertEqual(get_longest_words(self.string_14), 'same same')
        self.assertEqual(get_longest_words(self.string_15), 'same')

    def test_count_repetitions(self):
        self.assertEqual(count_repetitions(self.string_1), '{\'a\': 3, \'r\': 2, \'t\': 1}')
        self.assertEqual(count_repetitions(self.empty_string), '{}')
        self.assertEqual(count_repetitions(self.string_without_letters), '{}')
