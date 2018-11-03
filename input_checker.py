

def rem_space_specialchar(string):
    string = ''.join(l for l in string if l.isalnum())
    if string.isalnum():
        return string        
    return None

def present_options_collect_response(options_list):
    for item in options_list:
        print(item)
    input_answer = input()
    return input_answer
    
    
#there is a problem in how the words of lists are identified - I think I did something funny in how I saved which list was active or how the list id is found... 
