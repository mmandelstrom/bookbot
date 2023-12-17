def main():
    book = "books/frankenstein.txt"
    text = get_text(book)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    letters_sorted_list = dict_to_sorted_list(letter_count)
    print(f"Book report for {book}")
    print(f"{word_count} found in {book}")

    for item in letters_sorted_list:
        if not item["letter"].isalpha():                
            continue
        print(f"The letter '{item['letter']}' was found {item['num']} times")
    

def get_text(book):
    with open(book) as f:
        return f.read()
        

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letter_count = {}

    for letter in text:
        letter = letter.lower()
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def dict_to_sorted_list(num_letters_dict):
    sorted = []

    for letter in num_letters_dict:
        sorted.append({"letter": letter, "num": num_letters_dict[letter]})
    sorted.sort(key=lambda x: x["num"], reverse=True)
    return sorted



main()
