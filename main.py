def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_text = get_book_text(frankenstein_path)
    frankenstein_word_count = count_words(frankenstein_text)
    frankenstein_letter_count = count_letters(frankenstein_text)
    sorted_frankenstein_letter_count = sort_letter_count(frankenstein_letter_count)

    book_report(frankenstein_path, frankenstein_word_count, sorted_frankenstein_letter_count)


def get_book_text(book_path):
    with open(book_path) as text:
        return text.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count

def sort_letter_count(dict):
    def sort_on(dict):
        return dict["count"]
    
    def create_dict_list(dict):
        dict_list = []
        for key in dict:
            if key.isalpha():
                dict_list.append({"char": key, "count": dict[key]})
        return dict_list
    
    list_of_dict = create_dict_list(dict)
    list_of_dict.sort(reverse=True, key=sort_on)

    return list_of_dict

def book_report(path, word_count, letter_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document \n")
    for dict in letter_count:
        char = dict["char"]
        count = dict["count"]
        print(f"The '{char}' character was found {count} times")
    print("\n--- End Report ---")
    pass

main()