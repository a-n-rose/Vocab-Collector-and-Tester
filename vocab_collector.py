import sqlite3


class Collect_Vocab:
    def __init__(self):
        self.database = 'vocab_lists'
        self.conn = sqlite3.connect(self.database)
        self.c = self.conn.cursor()
        self.c.execute("")
        
    def access_users_table(self):
        msg = '''CREATE TABLE IF NOT EXISTS users(username text)'''
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
            return True
        elif len(user_there) == 0:
            return False
        return None
        
    def add_user(self):
        t = (self.username,)
        msg = '''INSERT INTO users VALUES (?) '''
        self.c.execute(msg,t)
        self.conn.commit()
        exist = self.check_if_user_exists()
        return exist
