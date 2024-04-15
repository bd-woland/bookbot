def get_file_contents(path):
    with open(path) as f:
        return f.read()

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

def print_report(path, word_count, count_by_char):
    print(f'--- Begin report of {path} ---')
    print(f'{word_count} words found in the document')
    print()
    for char, char_count in count_by_char.items():
        print(f'The \'{char}\' character was found {char_count} times')

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

def main():
    path = 'books/frankenstein.txt'

    file_contents = get_file_contents(path)

    word_count = count_words(file_contents)
    count_by_letter = sort_by_value(filter_alnum_keys(count_characters(file_contents)))

    print_report(path, word_count, count_by_letter)

main()
