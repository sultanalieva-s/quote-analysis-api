def count_total_vowels_consonants(quote):
    quote = quote.lower()

    total_letters_counter = 0
    total_vowels_counter = 0
    total_consonant_counter = 0

    vowels = {"a": True, "e": True, "u": True, "i": True, "o": True}
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


def count_average_word_length(quote):
    if not quote:
        return 0
    words = quote.strip().split(" ")
    len_sum = 0
    divider = len(words)

    has_letters = False
    for word in words:
        if word[0].isalpha():
            has_letters = True
            len_sum += len(word)
        else:
            divider -= 1

    if not has_letters:
        return 0

    avg = len_sum // divider
    return avg


def get_longest_words(quote):
    words = quote.split(" ")
    max_lengths = []
    c = 3
    # TODO: refactor the if statement
    if len(words) == 0 or len(words) == 1 or len(words) == 2 or len(words) == 3:
        c = len(words)
    while c:
        max_length = 0
        max_length_word_index = 0

        for i in range(0, len(words)):
            if len(words[i]) > max_length:
                max_length = len(words[i])
                max_length_word_index = i

        max_lengths.append(words[max_length_word_index])
        words.pop(max_length_word_index)
        c -= 1
    return ' '.join(max_lengths)


def count_repetitions(quote):
    quote = quote.lower().strip()
    letters = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    for i in quote:
        if i.isalpha():
            letters[i] += 1

    return str({key: val for key, val in letters.items() if val != 0})
