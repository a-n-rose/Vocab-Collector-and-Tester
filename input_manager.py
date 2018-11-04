

def rem_space_specialchar(string):
    string = ''.join(l for l in string if l.isalnum())
    if string.isalnum():
        return string        
    return None

    
def get_word_info():
    print("New word: ")
    word = input()
    print("Meaning: ")
    meaning = input()
    print("Example sentence (if multiple, separate by ; ) ")
    example = input()
    print("Tags (separated by ;)")
    tags = input()
    return word, meaning, example, tags


def get_list_info():
    print("Name of list: ")
    name = input()
    print("Tags (separated by ;)")
    tags = input()
    return name, tags
