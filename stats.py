def get__book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_count = {}
    text = text.lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_dictionary(chars):
    new_list = [{"char": k, "num": v} for k, v in chars.items() if k.isalpha()]
    new_list.sort(key=lambda x: x["num"], reverse=True)
    for item in new_list:
        print(f"{item["char"]}: {item['num']}")


