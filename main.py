def main():

    book_path = 'books/frankenstein.txt'
 
    def get_book_text(path):
        with open(path) as f:
            file_contents = f.read()
        return file_contents


    def word_count(str):
        words = str.split()
        return(len(words))
    
    def count_characters(str):
        result = {}
        for s in str:
            if s not in result:
                result[s] = 1
            else:
                result[s] += 1
        return result
    
    def create_list_of_dicts(dict):
        dict_list = []
        for key, value in dict.items():
             if key.isalpha():
                dict_list.append({key: value})
        return dict_list
    
    def sort_on(dict_item):
        return list(dict_item.values())[0]
    
    def print_report(dict_list):
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_of_words} found in the doc""\n")
        for dict in dict_list:
            for key, value in dict.items():
                print(f"The {key} character was found {value} times")
    
    book_text = get_book_text(book_path)
    num_of_words = word_count(book_text)
    book_text_lower = book_text.lower()
    count_characters(book_text_lower)
    counted_characters = count_characters(book_text_lower)
    dict_list = create_list_of_dicts(counted_characters)
    dict_list.sort(reverse=True, key=sort_on)
    print_report(dict_list)

main()