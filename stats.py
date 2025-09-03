def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):

    words = text.split()
    return len(words)

def character_count(text):
    char_dict = {}
    for char in text.lower():
        if char.isalpha() == True:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_list(text):
    old_dict = character_count(text)
    list = []
    final_list = []
    for index in old_dict:
        dict = {"char": index, "num": old_dict[index]}
        list.append(dict)
    sorted_list = sorted(list,reverse=True, key = lambda num: num['num'])
    return sorted_list
