# Vocab-Collector-and-Tester
My own personal vocabulary collector. Work in progress. Collect words in different languages in different lists. These are saved to a database via SQLite3.  Create quizes w write-in options, multiple choice, "flashcards".

EDIT: I've randomly decided to play with this again and cleaned it up using Poetry. It's good enough to help preserve my German. We'll see if I further improve on it.

## Using the program

The main menu is 'action_list' which asks the user if they would like to start a new list or look at an already created list. If there is no list yet created, the user is prompted to create one. Each list has a name and tags the user can specify.

In each list, the user is given a 'action_word' menu, where they can choose to add a new word, review the words in the list, or to change to a different list; the latter option will send them back to the 'action_list' menu.

For a new word, the user can also add a meaning (future versions should allow user to edit this meaning, e.g. add a meaning in later), example sentences, and tags. 

To review words, the user has the options of 1) flashcards, 2) multiple choice, 3) fill-in-the-blank, 4) print out of all word-meaning pairs.

At almost every input instance the user can type in 'exit' to close the application. 

## Example: Running the program for the first time

```
Username: 
Spaces and special characters will be removed: cactus

Your username will be saved as 'cactus'

Welcome cactus! Enter a password to create your account

Password: 
1357

You're account has been created.
Get started by creating your first list.


For each list of words you create, you can add tags and example sentences.

You can even test your knowledge with flashcards, multiple choice and fill-in-the-blank quizzes.


Action:
1) open existing list
2) create new list
Enter 1 or 2 (or exit): 2
Name of list: 
German
Tags (separated by ;)
maintain fluency

Action:
1) add word
2) review words 
3) change list
Enter 1, 2, 3 (or exit): 1
New word: 
der Autofrachter
Meaning: 
car carrier
Example sentence (if multiple, separate by ; ) 
Demnächst kommt aber der Autofrachter von BYD nach Deutschland, um Autos in Deutschand zu verkaufen.
Tags (separated by ;)
trade; economics; transportation

```
## Example: Reviewing words

```

Action:
1) add word
2) review words 
3) change list
Enter 1, 2, 3 (or exit): 2

Review:
1) Flashcards
2) Multiple Choice
3) Fill in the blank
4) View all words and their meanings
Enter 1, 2, 3, 4 (or exit): 2

Which of the meanings below (enter the corresponding number) best matches this word: 

das Nachspiel

1 --> car carrier

2 --> aftermath

3 --> in this country

2

Great job!


Which of the meanings below (enter the corresponding number) best matches this word: 

hierzulande

1 --> aftermath

2 --> in this country

3 --> car carrier

2

Great job!


Which of the meanings below (enter the corresponding number) best matches this word: 

der Autofrachter

1 --> aftermath

2 --> in this country

3 --> car carrier

3

Great job!


Your score: 100.0% 
Perfect score! I think you gotta find some harder words.

Action:
1) add word
2) review words 
3) change list
Enter 1, 2, 3 (or exit): 


```

## To Run:

### Download / Clone Repo

Put the scripts in this repo into desired Directory.

### Install Python3 and Poetry

If you don't have Python3 installed, make sure it's on your computer. I used Python3.5 to build this.

### Get into the correct directory

```
$ cd ./Vocab-Collector-and-Tester/
```

### Start Virtual Environment

If you don't have one yet, first enter this:
```
$ python3 -m venv env
```

To start the environment:
```
$ source env/bin/activate
(env)...$
```

### Additional Installations: Access poetry lock file

So far I only need to install Numpy and Pytest
```
(env)...$ cd ./vocabtrainer/
(env)...$ poetry install
```

To run tests with poetry:

```
(env)...$ poetry run pytest
```

### Run Main Module

You should then be able to run the package. Sorry for changing directories so often:

```
(env)...$ cd ..
(env)...$ python3 vocab_run.py 
```

## Current State:

The user can:
* create account with non-protected password
* create multiple lists with tags
* add new words with a meaning, example sentences, tags
* view the word - meaning pairs in each list
* test knowledge via flashcard, fill-in-the-blank, or multiple choice quizzes 
* navigate between functionalities quite easily as well as exit at almost any input instance
* run tests on the application

## ToDo:
* improve quiz functionality (account for the complexities of language)
* add tag sorting functionality
* add columns in databases for 'last tested' and 'performance'. --> can create lists based on words/lists with poor performance
* add editing capabilities

