def count_words(text):
    return len(text.split())
def count_characters(text):
    characters = {}
    letter_list = list(text)
    for letter in letter_list:
        lowercase_letter = letter.lower()
        if lowercase_letter in characters:
            characters[lowercase_letter] = characters[lowercase_letter] + 1
        else:
            characters[lowercase_letter] = 1
    return characters
def sort_on(dict):
    return dict["num"]
def dict_sort(dict):
    characters = []
    for key in dict:
        character = {}
        character["name"] = key
        character["num"] = dict[key]
        characters.append(character)
    characters.sort(reverse=True, key=sort_on)
    return characters



        




    