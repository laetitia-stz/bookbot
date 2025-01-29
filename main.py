# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     print(text)


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()

# main()

# def count_words():
#     with open("books/frankenstein.txt") as f:
#         words = f.read().split()
#     return len(words)

# print("There is", count_words(), "words")  


# def count_characters():
#     with open("books/frankenstein.txt") as f:
#         book = f.read()
#         lowered_characters = book.lower()
    
#     character_count = {}

#     for character in lowered_characters:
#         if character in character_count:
#             character_count[character] += 1
#         else: 
#             character_count[character] = 1

#     return character_count
    
# print(count_characters())


def count_characters_and_words():
    with open("books/frankenstein.txt") as f:
        book = f.read()
        lowered_characters = book.lower()
        
        character_count = {}
        word_count = 0

        for character in lowered_characters:
            if character.isalpha():
                if character in character_count:
                    character_count[character] += 1
                else: 
                    character_count[character] = 1

        word_count = len([word for word in lowered_characters.split() if word.isalpha()])

        sorted_char_count = sorted(character_count.items(), key=lambda x: x[1], reverse=True)

        return word_count, sorted_char_count
    

def print_report():
    word_count, sorted_char_count = count_characters_and_words()
    
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    print(f"--- End report ---")

print_report()

