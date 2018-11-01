import sqlite3


class Collect_Vocab:
    def __init__(self):
        self.database = 'vocab_lists'
        self.conn = sqlite3.connect(self.database)
        self.c = self.conn.cursor()
        self.c.execute("")
        
    def access_users_table(self):
        msg = '''CREATE TABLE IF NOT EXISTS users(user_id integer primary key, username text)'''
        self.c.execute(msg)
        self.conn.commit()
        return None
    
    def check_if_user_exists(self):
        self.access_users_table()
        self.c.execute('''SELECT * FROM users''')
        users = self.c.fetchall()
        print(users)
        user_there = [item for item in users if self.username in item]
        if len(user_there) == 1:
            self.user_id = user_there[0][0]
            print(self.user_id)
            return True
        elif len(user_there) == 0:
            return False
        return None
        
    def add_user(self):
        t = (self.username,)
        msg = '''INSERT INTO users VALUES (NULL,?) '''
        self.c.execute(msg,t)
        self.conn.commit()
        exist = self.check_if_user_exists()
        return exist
    
    def access_user_vocablists(self):
        msg = '''CREATE TABLE IF NOT EXISTS vocab_lists(list_id integer primary key, list_name text, language text, tags text, list_user_id integer, FOREIGN KEY(list_user_id) REFERENCES users(user_id) )'''
        self.c.execute(msg)
        self.conn.commit()
        return None
    
    def choose_list(self):
        print("\nHere are your lists")
        available_nums = []
        for key, value in self.dict_lists.items():
            print(value,') ',key)
            available_nums.append(value)
        print("\nTable of interest: (enter corresponding number) ")
        curr_list_id = int(input())
        if curr_list_id in available_nums:
            self.curr_list_id = curr_list_id
            print("Chosen list id is: {}".format(curr_list_id))
        else:
            print("\nPlease choose a corresponding number\n".upper())
            self.choose_list()
        return None
    
    def create_new_list(self):
        print("Name of list: ")
        name = input()
        print("Language: ")
        lang = input()
        print("Tags (separated by ;)")
        tags = input()
        msg = '''INSERT INTO vocab_lists VALUES (NULL, ?,?,?,?) '''
        t = (name,lang,tags,self.user_id)
        self.c.execute(msg,t)
        self.conn.commit()
        return None
        
    def check_lists(self):
        self.access_user_vocablists()
        msg = '''SELECT * FROM vocab_lists WHERE list_user_id=%s ''' % self.user_id
        self.c.execute(msg)
        lists = self.c.fetchall()
        if len(lists) == 0:
            print("It looks like you don't have a list. Start one now!")
            self.create_new_list()
            self.check_lists()
        else:
            self.dict_lists = {}
            for list_index in range(len(lists)):
                name_of_list = lists[list_index][1]
                self.dict_lists[name_of_list] = list_index+1
            self.choose_list()
        return None
        
    def access_word_table(self):
        msg = '''CREATE TABLE IF NOT EXISTS words(word_id integer primary key, word text, meaning text, tags text, word_list_id integer, FOREIGN KEY(word_list_id) REFERENCES vocab_lists(list_id)) '''
        self.c.execute(msg)
        self.conn.commit()
        return None
    
    def add_word(self):
        self.access_word_table()
        print("New word: ")
        word = input()
        print("Meaning: ")
        meaning = input()
        print("Tags (separated by ;)")
        tags = input()
        msg = '''INSERT INTO words VALUES (NULL, ?,?,?,?) '''
        t = (word,meaning,tags,self.curr_list_id)
        self.c.execute(msg,t)
    
    def quiz_flashcard(self):
        print("Currently in the works!")
        pass
    
    def quiz_multchoice(self):
        print("Multiple choice quizzing is in the works. Try Flashcards!")
        self.quiz_flashcard()
        return None
    
    def quiz_fillblank(self):
        print("Fill-in-the-blank quizzing is in the works. Try Flashcards!")
        self.quiz_flashcard()
        return None
    
    def quiz_wordlist(self):
        print("\nQuiz:\n1) Flashcards\n2) Multiple Choice\n3) Fill in the blank")
        quiz_type = int(input("Enter 1, 2, or 3: "))
        if quiz_type == 1:
            self.quiz_flashcard()
        elif quiz_type == 2:
            self.quiz_multchoice()
        elif quiz_type == 3:
            self.quiz_fillblank()
        else:
            print("\nPlease enter 1, 2, or 3\n".upper())
            self.quiz_wordlist()
        return None
        
    def action_word(self):
        print("\nAction:\n1) add word\n2) review words")
        action_int = int(input("Enter 1 or 2: "))
        if action_int == 1:
            self.add_word()
        elif action_int == 2:
            self.quiz_wordlist()
        else:
            print("\nPlease enter 1 or 2\n".upper())
            self.action_word()
        return None
    
    def action_list(self):
        print("\nAction:\n1) open existing list\n2) create new list")
        action_int = int(input("Enter 1 or 2: "))
        if action_int == 1:
            self.check_lists()
        elif action_int == 2:
            self.create_new_list()
            self.check_lists()
        else:
            print("\nPlease enter 1 or 2\n".upper())
            self.action_list()
        return None
        
