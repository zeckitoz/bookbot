from stats import *
path = "books/frankenstein.txt"

def main():
    text = get__book_text(path)
    words = count_words(text)
    chars = count_chars(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    sort_dictionary(chars)
    print("============= END ===============")

if __name__ == "__main__":
    main()