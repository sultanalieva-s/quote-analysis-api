def count_total_vowels_consonants(quote):
    quote = quote.lower()
    total_letters_counter = 0
    total_vowels_counter = 0
    total_consonant_counter = 0
    vowels = dict({"a": 0, "e": 0, "y": 0, "u": 0, "i": 0, "o": 0})
    consonants = dict(
        {
            "q": 0,
            "w": 0,
            "r": 0,
            "t": 0,
            "y": 0,
            "p": 0,
            "s": 0,
            "d": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "z": 0,
            "x": 0,
            "c": 0,
            "v": 0,
            "b": 0,
            "n": 0,
            "m": 0,
        }
    )
    for i in quote:
        if i.isalpha():
            total_letters_counter += 1

        if not vowels.get(i):
            total_vowels_counter += 1

        if not consonants.get(i):
            total_consonant_counter += 1

    return {
        "total_letters": total_letters_counter,
        "total_vowels": total_vowels_counter,
        "total_consonants": total_consonant_counter,
    }


def count_repetitions(quote):
    return "Test"


def count_average_word_length(quote):
    words = quote.split(" ")
    len_sum = 0

    for word in words:
        len_sum += len(word)

    avg = len_sum / len(words)
    return round(avg, 2)


def get_longest_words(quote):
    words = quote.split(" ")
    max_lens = []
    c = 3
    while c:
        max_len = 0
        index_to_delete = 0

        for i in range(0, len(words)):
            if len(words[i]) > max_len:
                max_len = len(words[i])
                index_to_delete = i

        max_lens.append(max_len)
        # words.pop(index_to_delete)
        c -= 1
    return ''
