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
from errors import ExitApp

if __name__ == "__main__":
    try:
        cv = Collect_Vocab()
        cv.sign_in()
        while cv.is_user == True:
            cv.action_list()
            
    except ExitApp as e:
        print(e)
    except Exception as e:
        print("Error Occurred: {}".format(e))
        traceback.print_tb(e)
        
    finally:
        if cv.conn:
            cv.conn.close()
