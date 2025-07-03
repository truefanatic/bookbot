def get_file_content(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def get_num_words(path_to_file):
    return len(get_file_content(path_to_file).split())


def get_char_count(path_to_file):
    content = get_file_content(path_to_file).lower()
    dictionary = {}
    for char in content:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary


def sort_dict(dict): 
    list_dict = []

    def sort_on(items):
        return items["num"]
    
    for key in dict:
        if key.isalpha():
            list_dict.append({"char": key, "num": dict[key]})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict