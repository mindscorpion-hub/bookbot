import sys
from stats import get_word_count, get_book_text, get_letter_count, letter_format, sort_on

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
       
    book_text = get_book_text(f"{sys.argv[1]}")
    word_count = get_word_count(book_text)
    letter_count = get_letter_count(book_text)
    formatted = letter_format(letter_count)

    formatted.sort(reverse=True, key=sort_on)
     
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for i in formatted:
        if i["char"].isalpha():
            print(f"{i["char"]}:", i["num"])
        else:
            pass

    print("============= END ===============")


main()

