from stats import get_word_count, get_book_text, get_letter_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    letter_count = get_letter_count(book_text)

    print(f"Found {word_count} total words")

    for i in letter_count:
        print(f"'{i}':",letter_count[i])

  
main()

