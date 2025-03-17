def count_words(string):
    return len(string.split())

def count_characters(string):
    count_by_char = {}

    for char in string.lower():
        if (char in count_by_char):
            count_by_char[char] += 1
        else:
            count_by_char[char] = 1
    
    return count_by_char

def is_alnum_key(item):
    key, value = item

    return key.isalpha()

def filter_alnum_keys(dictionary):
    return dict(filter(is_alnum_key, dictionary.items()))

def sort_by_value(dictionary, reverse = True):
    return dict(sorted(
        dictionary.items(),
        key = lambda item : item[1],
        reverse = reverse
    ))
