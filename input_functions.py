import re
import sys

def get_username():
    print("Username: ")
    username = input()
    username = prep_username(username)
    if username:
        return username
    else:
        get_username()

def prep_username(username):
    username_checked = ''.join(l for l in username if l.isalnum())
    if username_checked.isalnum():
        return username_checked
    else:
        print("Please use letters and numbers only. Spaces and special characters will be removed.")
        return None
