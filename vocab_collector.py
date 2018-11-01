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
    
    def print_lists(self):
        self.access_user_vocablists()
        msg = '''SELECT * FROM vocab_lists WHERE list_user_id=%s ''' % self.user_id
        self.c.execute(msg)
        lists = self.c.fetchall()
        if len(lists) == 0:
            print("It looks like you don't have a list. Start one now!")
            self.create_new_list()
            self.print_lists()
        print(lists)
        print(lists[0][4])
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
    
    def choose_table(self):
        pass
        
    def access_word_table(self):
        msg = '''CREATE TABLE IF NOT EXISTS words(word_id integer primary key, word text, meaning text, tags text, word_list_id integer, FOREIGN KEY(word_list_id) REFERENCES vocab_lists(list_id)) '''
        self.c.execute(msg)
        self.c.commit()
        return None
    
    #def add_word(self):
        #print("New word: ")
        #word = input()
        #print("Meathing: ")
        #meaning = input()
        #print("Tags (separated by ;)")
        #tags = input()
        #msg = '''INSERT INTO words VALUES (NULL, ?,?,?,?) '''
        #t = (word,meaning,tags,self.curr_list_id)
        #self.c.execute(msg,)
        
    
