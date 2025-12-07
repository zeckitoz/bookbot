from stats import *
def main():
    text = get__book_text("books/frankenstein.txt")
    words = count_words(text)
    print(f"Found {words} total words")
    chars = count_chars(text)
    print(chars)

if __name__ == "__main__":
    main()