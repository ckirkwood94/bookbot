def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_text = get_book_text(frankenstein_path)
    # print(get_book_text(frankenstein_path))
    print(count_words(frankenstein_text))


def get_book_text(book_path):
    with open(book_path) as text:
        return text.read()
    
def count_words(text):
    words = text.split()
    return len(words)

main()