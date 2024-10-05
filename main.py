def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        return(word_count)

def get_diff_letter_amount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        letter_count = {}
        for letter in file_contents:
            lowered_letter = letter.lower()
            if lowered_letter.isalpha():
                if lowered_letter in letter_count:
                    letter_count[lowered_letter] += 1
                else:
                    letter_count[lowered_letter] = 1
        converted_dict = [{"char": char, "count": count}
        for char, count in letter_count.items()]
        return(converted_dict)

def sort_on(dict):
    return dict["count"]

def sort_dictionary():
    letter_dictionary = get_diff_letter_amount()
    letter_dictionary.sort(reverse=True, key=sort_on)
    return(letter_dictionary)

def print_report():
    print("--- Begin report of books/frankenstein.txt ---")
    print()
    words = main()
    final_dict = sort_dictionary()
    print(f"There are a total of {words} words in this book!")
    print()
    for item in final_dict:
        print(f"The '{item['char']}' character was found {item['count']} times!")
    print()
    print("--- Ending report of books/frankenstein.txt ---")

print_report()