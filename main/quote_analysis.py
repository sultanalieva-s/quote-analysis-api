def count_total_vowels_consonants(quote):
    quote = quote.lower()

    total_letters_counter = 0
    total_vowels_counter = 0
    total_consonant_counter = 0

    vowels = {"a": True, "e": True, "y": True, "u": True, "i": True, "o": True}
    consonants = {
        "q": True,
        "w": True,
        "r": True,
        "t": True,
        "y": True,
        "p": True,
        "s": True,
        "d": True,
        "f": True,
        "g": True,
        "h": True,
        "j": True,
        "k": True,
        "l": True,
        "z": True,
        "x": True,
        "c": True,
        "v": True,
        "b": True,
        "n": True,
        "m": True,
    }

    for i in quote:
        if i.isalpha():
            total_letters_counter += 1

        if vowels.get(i, False):
            total_vowels_counter += 1

        if consonants.get(i, False):
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
    return ""
