

def rem_space_specialchar(string):
    string = ''.join(l for l in string if l.isalnum())
    if string.isalnum():
        return string        
    return None

    
