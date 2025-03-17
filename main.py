import sys

from stats import count_characters, count_words, filter_alnum_keys, sort_by_value

def get_file_contents(path):
    with open(path) as f:
        return f.read()

def print_report(path, word_count, count_by_char):
    print('============ BOOKBOT ============')
    print(f'--- Analyzing book found at {path} ---')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for char, char_count in count_by_char.items():
        print(f'{char}: {char_count}')
        
    print('============= END ===============')

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')

        sys.exit(1)

    path = sys.argv[1]

    file_contents = get_file_contents(path)

    word_count = count_words(file_contents)
    count_by_letter = sort_by_value(filter_alnum_keys(count_characters(file_contents)))

    print_report(path, word_count, count_by_letter)

main()
