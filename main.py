def count_characters(word_list):
    chars = {}
    for word in word_list:
        word = word.lower()
        for c in word:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    return chars

def print_report(word_list, char_map):
    print("--- Brgin report of books/frankenstein.txt ---")
    print(f"{len(word_list)} words found in the document")
    print()
    char_list = []
    for k in char_map:
        if k.isalpha():
            char_list.append((k, char_map[k]))
    char_list.sort(reverse=True, key=lambda k: k[1])
    for c in char_list:
        print(f"The '{c[0]}' character was found {c[1]} times")


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    char_map = count_characters(words)
    print_report(words, char_map)