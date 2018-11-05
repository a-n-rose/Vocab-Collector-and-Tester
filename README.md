# Vocab-Collector-and-Tester
My own personal vocabulary collector. Work in progress. Collect words in different languages in different lists. These are saved to a database via SQLite3.  Create quizes w write-in options, multiple choice, "flashcards".

## To Run:
Installations: 

I used Python 3.5 and Numpy 1.15.3 to build this app.

Once those are installed and necessary scripts downloaded, enter into the command line:
```
$ python3 vocab_run.py 
```

The main menu is 'action_list' which asks the user if they would like to start a new list or look at an already created list. If there is no list yet created, the user is prompted to create one. Each list has a name and tags the user can specify.

In each list, the user is given a 'action_word' menu, where they can choose to add a new word, review the words in the list, or to change to a different list; the latter option will send them back to the 'action_list' menu.

For a new word, the user can also add a meaning (future versions should allow user to edit this meaning, e.g. add a meaning in later), example sentences, and tags. 

To review words, the user has the options of 1) flashcards, 2) multiple choice, 3) fill-in-the-blank, 4) print out of all word-meaning pairs.

At almost every input instance the user can type in 'exit' to close the application. 


## Current State:

The user can:
* create account with non-protected password
* create multiple lists with tags
* add new words with a meaning, example sentences, tags
* view the word - meaning pairs in each list
* complete a fill-in-the-blank test for each list and earn a score
* test knowledge via flashcard, fill-in-the-blank, or multiple choice quizes 
* navigate between functionalities quite easily as well as exit at almost any input instance

## ToDo:
* further separate/organize functions --> apply test to them
* improve quiz functionality (account for the complexities of language)
* add tag sorting functionality
* add columns in databases for 'last tested' and 'performance'. --> can create lists based on words/lists with poor performance
* add editing capabilities
* check that list names don't conflict/already exist
