from stats import get_num_words, get_char_count, sort_dict
import sys


def main():
    if len(sys.argv)!= 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    num_words = get_num_words(book_path)
    dict = get_char_count(book_path)
    sorted_dict = sort_dict(dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted_dict:
        val = list(d.values())
        print(val[0] + ": " + str(val[1]))
    print("============= END ===============")


main()
