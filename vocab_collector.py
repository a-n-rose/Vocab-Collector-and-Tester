import sqlite3        
import re
from errors import ExitApp
from input_manager import rem_space_specialchar, get_word_info, get_list_info


class Collect_Vocab:
    def __init__(self):
        self.database = 'vocab_lists.db'
        self.conn = sqlite3.connect(self.database)
        self.c = self.conn.cursor()
        
        
# Set up the user's account: logging in or registering

    def get_username(self):
        print("\nUsername: ")
        username = input("Spaces and special characters will be removed: ")
        username = rem_space_specialchar(username)
        if username:
            return username
        else:
            print("Not enough alphanumeric characters used. Try again.")
            self.get_username()
        return None
    
    def get_password(self):
        print("\nPassword: ")
        password = input("Spaces and special characters will be removed: ")
        password = rem_space_specialchar(password)
        if password:
            return password
        else:
            print("Not enough alphanumeric characters used. Try again.")
            self.get_password()
        return None
    
    def login(self,username):
        print("\nWelcome back {}! Enter your password to access your lists.".format(username))
        password = self.get_password()
        if password:
            self.check_password(username, password)
            if self.is_user == True:
                return True
            else:
                return False
        
    def register(self,username):
        print("\nWelcome {}! Enter a password to create your account".format(username))
        password = self.get_password()
        if password:
            self.add_user(username,password)
            return True
        else:
            return False

    def sign_in(self):
        username = self.get_username()
        exist, user_id = self.check_if_user_exists(username)
        if exist == False:
            logged_in = self.register(username)
        else:
            logged_in = self.login(username)
        return None
        
    def access_users_table(self):
        msg = '''CREATE TABLE IF NOT EXISTS users(user_id integer primary key, username text, password text)'''
        self.c.execute(msg)
        self.conn.commit()
        return None
    
    def check_if_user_exists(self,username):
        self.access_users_table()
        t = (username,)
        self.c.execute('''SELECT * FROM users WHERE username=? ''', t)
        users = self.c.fetchall()
        #print(users)
        if len(users) == 1:
            return True, users[0]
        elif len(users) == 0:
            return False, None
        return None, None
    
    def check_password(self,username, password):
        t = (username,)
        msg = '''SELECT password FROM users WHERE username=? ''' 
        self.c.execute(msg,t)
        real_password = self.c.fetchall()[0][0]
        #print("password = {}\nreal password = {}".format(password, real_password))
        if password == real_password:
            self.is_user = True
            self.username = username
            _, self.user_id = self.check_if_user_exists(username)
        else:
            self.is_user = False
        return None
        
    def add_user(self,username,password):
        self.username = username
        t = (username,password,)
        msg = '''INSERT INTO users VALUES (NULL,?,?) '''
        self.c.execute(msg,t)
        self.conn.commit()
        self.is_user, self.user_id = self.check_if_user_exists(username)
        print("\nWelcome {}! We're glad you're here.\n".format(username))
        return None
    
    
# Actions the logged_in user can do:
    
    def action_list(self):
        if self.is_user == True:
            print("\nAction:\n1) open existing list\n2) create new list")
            action_int = input("Enter 1 or 2 (or exit): ")
            action_int = rem_space_specialchar(action_int)
            if action_int.isdigit():
                if int(action_int) == 1:
                    self.check_lists()
                    self.action_word()
                elif int(action_int) == 2:
                    list_name,list_tags = get_list_info()
                    self.create_new_list(list_name,list_tags)
                    self.check_lists()
            else:
                if 'exit' in action_int.lower():
                    self.is_user = False
                    self.action_list()
                else:
                    print("\nPlease enter 1 or 2\n".upper())
                    self.action_list()
        else:
            raise ExitApp("Good job learning words! Until the next time :)")
        return None
    
    def action_word(self):
        print("\nAction:\n1) add word\n2) review words \n3) change list")
        action_int = input("Enter 1, 2, 3 (or exit): ")
        action_int = rem_space_specialchar(action_int)
        if action_int.isdigit():
            if int(action_int) == 1:
                self.add_word()
                self.action_word()
            elif int(action_int) == 2:
                self.quiz_wordlist()
            elif int(action_int) == 3:
                self.action_list()
        else:
            if 'exit' in action_int.lower():
                self.is_user = False
                self.action_list()
            else:
                print("\nPlease enter 1 or 2\n".upper())
                self.action_word()
        return None
    
    def access_user_vocablists(self):
        msg = '''CREATE TABLE IF NOT EXISTS vocab_lists(list_id integer primary key, list_name text, list_number int, tags text, list_user_id integer, FOREIGN KEY(list_user_id) REFERENCES users(user_id) )'''
        self.c.execute(msg)
        self.conn.commit()
        return None
    
    def choose_list(self):
        print("\nHere are your lists")
        for key, value in self.dict_lists.items():
            print(value[1],'--> ',key)
        print("\nTable of interest: (enter the corresponding number) ")
        curr_list_num = input()
        curr_list_num = rem_space_specialchar(curr_list_num)
        if curr_list_num.isdigit():
            curr_list_num = int(curr_list_num)
        else:
            if 'exit' in curr_list_num.lower():
                self.is_user = False
                self.action_list()
            else:
                print("\nPlease enter the corresponding number\n".upper())
        for key,value in self.dict_lists.items():
            if curr_list_num == value[1]:
                self.curr_list_id = value[0]
                print("The current list ID is: {}".format(self.curr_list_id))
            else:
                print("\nPlease choose a corresponding number\n".upper())
                self.choose_list()
        return None
    
    def coll_user_vocab_lists(self):
        self.access_user_vocablists()
        t = (str(self.user_id),)
        msg = '''SELECT * FROM vocab_lists WHERE list_user_id=? ''' 
        self.c.execute(msg, t)
        lists = self.c.fetchall()
        return lists
    
    def check_lists(self):
        lists = self.coll_user_vocab_lists()
        if len(lists) == 0:
            print("It looks like you don't have a list. Start one now!")
            name,tags = get_list_info()
            self.create_new_list(name,tags)
            self.check_lists()
        else:
            self.dict_lists = {}
            for list_index in range(len(lists)):
                name_of_list = lists[list_index][1]
                self.dict_lists[name_of_list] = (lists[list_index][0],lists[list_index][2])
            self.choose_list()
        return None
    
    def get_list_id(self,list_name):
        t = (list_name,)
        msg = '''SELECT list_id FROM vocab_lists WHERE list_name=? '''
        self.c.execute(msg,t)
        list_id = self.c.fetchall()[0][0]
        return list_id
    
    def create_new_list(self,name,tags):
        lists = self.coll_user_vocab_lists()
        list_num = len(lists)+1
        msg = '''INSERT INTO vocab_lists VALUES (NULL, ?,?,?,?) '''
        t = (name,list_num,tags,str(self.user_id))
        self.c.execute(msg,t)
        self.conn.commit()
        self.curr_list_id = self.get_list_id(name)
        self.curr_list_name = name
        self.action_word()
        return None
        
    def access_word_table(self):
        msg = '''CREATE TABLE IF NOT EXISTS words(word_id integer primary key, word text, meaning text, example_sentence text, tags text, word_list_id integer, FOREIGN KEY(word_list_id) REFERENCES vocab_lists(list_id)) '''
        self.c.execute(msg)
        self.conn.commit()
        return None
    
    
    def add_word(self):
        self.access_word_table()
        word,meaning,example,tags = get_word_info()
        msg = '''INSERT INTO words VALUES (NULL, ?,?,?,?,?) '''
        if isinstance(self.curr_list_id,int):
            curr_list_id = str(self.curr_list_id)
        else:
            curr_list_id = self.curr_list_id
        t = (word,meaning,example,tags,curr_list_id)
        self.c.execute(msg,t)
        self.conn.commit()
        return None
    
    def quiz_flashcard(self):
        print("\nCurrently in the works!")
        self.action_word()
        return None
    
    def quiz_multchoice(self):
        print("\nMultiple choice quizzing is in the works. Try Flashcards!")
        self.quiz_flashcard()
        return None
    
    def quiz_fillblank(self):
        t = (str(self.curr_list_id))
        msg1 = '''SELECT example_sentence FROM words WHERE word_list_id=? '''
        msg2 = '''SELECT word FROM words WHERE word_list_id=? '''
        self.c.execute(msg1,t)
        examples = self.c.fetchall()
        self.c.execute(msg2,t)
        words = self.c.fetchall()
        print("\nWords: \n")
        for item_index in range(len(words)):
            print("\nExample sentences with {}:\n".format(words[item_index][0]))
            ex_list = re.split(';',examples[item_index][0])
            for sentence in ex_list:
                if ' ' == sentence[0]:
                    print('\n{}\n'.format(sentence[1:]))
                else:
                    print('\n{}\n'.format(sentence))            
        self.action_word()
        return None
    
    def show_words(self):
        print("\nWords in this list: ")
        t = (str(self.curr_list_id))
        msg = '''SELECT * FROM words WHERE word_list_id=? '''
        self.c.execute(msg,t)
        words = self.c.fetchall()
        if len(words) == 0:
            print("You haven't entered any words yet.")
        else:
            for word in words:
                print("{} : {}".format(word[1],word[2]))
        self.action_word()
        return None
    
    def quiz_wordlist(self):
        #create word table just in case one doesn't exist yet
        self.access_word_table()
        print("\nReview:\n1) Flashcards\n2) Multiple Choice\n3) Fill in the blank\n4) View all words and their meanings")
        quiz_type = input("Enter 1, 2, 3, 4 (or exit): ")
        if quiz_type.isdigit():
            if int(quiz_type) == 1:
                self.quiz_flashcard()
            elif int(quiz_type) == 2:
                self.quiz_multchoice()
            elif int(quiz_type) == 3:
                self.quiz_fillblank()
            elif int(quiz_type) == 4:
                self.show_words()
        else:
            if 'exit' in quiz_type.lower():
                self.is_user = False
                self.action_list()
            else:
                print("\nPlease enter 1, 2, 3, or 4\n".upper())
                self.quiz_wordlist()
        return None
