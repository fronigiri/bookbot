import sys
from stats import count_words
from stats import count_characters
from stats import dict_sort
def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    with open(args[1]) as f:
        file_contents = f.read()
    print(f"Analyzing book found at {args[1]}...")
    total_words = count_words(file_contents)
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    dictionary = count_characters(file_contents)
    characters = dict_sort(dictionary)
    for character in characters:
        if character["name"].isalpha():
            print(f"{character["name"]}: {character["num"]}")
    print("============= END ===============")
main()