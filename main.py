#Program that takes book as input and calculates number of words
from stats import get_book_text, get_number_words, get_letter_count, sorted_dicts
import sys

def main():

    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
        num_words = get_number_words(book_text)
        letter_count = get_letter_count(book_text)
        my_list = sorted_dicts(letter_count)
        

        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {sys.argv[1]}...')
        print('----------- Word Count ----------')
        print(f'Found {num_words} total words')
        print('--------- Character Count -------')
        
        for dict in my_list:
            print(f'{dict["char"]}: {dict["count"]}')

main()