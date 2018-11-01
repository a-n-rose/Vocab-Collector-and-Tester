'''
Functionality I want:

Run the program
Option:
~ new entry
~ learn

New Entry:
" word "  (first version: also enter word meaning)
--> add to list OR new list

Learn:
options: all words or from word lists

quiz options
~ flashcards (first version)
~ multiple choice 
~ fill in the blank

'''

from vocab_collector import Collect_Vocab
from input_functions import get_username
import traceback
from errors import AddUserError

if __name__ == "__main__":
    try:
        cv = Collect_Vocab()
        cv.username = get_username()
        user_exist = cv.check_if_user_exists()
        if user_exist == False:
            added = cv.add_user()
            if added != True:
                raise AddUserError("There seems to be an error in adding you to our database. We're sorry!")
            else:
                print("You've been added!")
        else:
            print("Welcome back {}!".format(cv.username))
        
        cv.check_lists()
        
    except AddUserError as aue:
        print(aue)
    except Exception as e:
        print("Error Occurred: {}".format(e))
        traceback.print_tb(e)
        
    finally:
        if cv.conn:
            cv.conn.close()
