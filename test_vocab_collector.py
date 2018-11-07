import os
import sqlite3
import unittest


#import class from module with my functions:
from vocab_collector import Collect_Vocab

class TestUserVocabDatabase(unittest.TestCase):
    '''
    Test the user vocab collection database
    '''
    
    def setUp(self):
        '''
        Setup a temporary database
        '''
        #create database
        self.db = Collect_Vocab('test_vocab.db')

        #create necessary tables
        msg = '''CREATE TABLE IF NOT EXISTS users(user_id integer primary key, username text, password text) '''
        self.db.c.execute(msg)
        self.db.conn.commit()
        
        msg = '''CREATE TABLE IF NOT EXISTS vocab_lists(list_id integer primary key, list_name text, list_number int, tags text, list_user_id integer, FOREIGN KEY(list_user_id) REFERENCES users(user_id) ) '''
        self.db.c.execute(msg)
        self.db.conn.commit()
        
        msg = '''CREATE TABLE IF NOT EXISTS words(word_id integer primary key, word text, meaning text, example_sentence text, tags text, word_list_id integer, FOREIGN KEY(word_list_id) REFERENCES vocab_lists(list_id)) '''
        self.db.c.execute(msg)
        self.db.conn.commit()
        
        
        
        #insert some data
        user1 = ('1','Stacey','sailboat')
        user2 = ('2','Freddy','fidgetspinner')
        
        #list name can also be included in 'tag search'
        user1_vocablist1 = ('1','German','1','every-day; beginner','1')
        user1_vocablist2 = ('4','Body Parts','2','German;intermediate','1')
        
        #can quiz user on multiple lists if they have the same name
        user2_vocablist1 = ('2','Colors','1','French;colors; beginner','2')
        user2_vocablist2 = ('3','Colors','2','Arabic;colors; beginner','2')
        
        vocablist1_words1 = ('1','Haus','house','Das Haus hat drei Schlafzimmer und zwei Badezimmer, perfekt für meine Familie; Er wollte sein Haus verkaufen weil es, ohne seine Kinder, zu groß war.','lifestyle; housing; accommodation','1')
        vocablist1_words2 = ('4','Frühstück','breakfast','Mein Magen morgens mag kein Frühstück; Zum Frühstück findet sie Pfannkuchen mit Ahornsirup am besten.','lifestyle; food; daily tasks','1')
        vocablist1_words3 = ('8','Büro','office','Meine Mama ist gerade im Büro weil sie einen Termin mit ihren Arbeitskollegen hat; Im Büro liegen alle meine Arbeitsunterlagen.','work; rooms;','1')
        
        vocablist2_words1 = ('2','bleu','blue',"Aujourd'hui, il n'y a pas de nuages et le ciel est bleu.;Il est ennuyeux que les vêtements d'enfants soient en rose ou en bleu. Il y a tellement d'autres couleurs là-bas!",'French; colors; easy','2')
        vocablist2_words2 = ('3','jaune','yellow',"Voici le bus scolaire jaune vif.;Le soleil émet en réalité plus de lumière verte que de lumière jaune.",'French; colors; intermediate','2')
        #to test the vocab app to find similar words in a sentence:
        #rouge --> rouges
        vocablist2_words3 = ('7','rouge','red',"Le ketchup a laissé plusieurs taches rouges sur le tapis.;Ses yeux sont rouges parce qu'il n'a pas dormi la nuit dernière.",'French; colors; plural; intermediate','2')
        
        
        #show limitations of app with non latin alphabets
        vocablist3_words1 = ('5','أزرق','blue',"السماء الزرقاء الصافية جميلة.",'Arabic; colors; easy','3')
        #The clear blue sky is beautiful. 
        vocablist3_words2 = ('6','الأصفر','yellow',"الشمس صفراء; الموز الأصفر",'Arabic; colors; intermediate','3')
        #the sun is yellow
        #bananas are yellow
        vocablist3_words3 = ('9','أحمر','red',"الدم ليس أزرق ولكن أحمر.;الورود هي حمراءالبنفسج هي زرقاء",'Arabic; colors; plural; intermediate','3')
        #the blood is red not blue
        #roses are red violets are blue
        
        #vocablist4 will remain empty
        
        
        msg = '''INSERT INTO users VALUES (?,?,?) '''
        self.db.c.executemany(msg,[user1,user2])
        self.db.conn.commit()
        
        msg = '''INSERT INTO vocab_lists VALUES (?,?,?,?,?)'''
        self.db.c.executemany(msg,[user1_vocablist1,user1_vocablist2,user2_vocablist1,user2_vocablist2])
        self.db.conn.commit()
        
        msg = '''INSERT INTO words VALUES (?,?,?,?,?,?) '''
        self.db.c.executemany(msg,[vocablist1_words1,vocablist1_words2,vocablist1_words3,vocablist2_words1,vocablist2_words2,vocablist2_words3,vocablist3_words1,vocablist3_words2,vocablist3_words3,])
        self.db.conn.commit()
        

        
    def tearDown(self):
        if self.db.conn:
            self.db.conn.close()
        os.remove("test_vocab.db")
        
        
        
    ##### TESTS FOR ESTABLISHING AND CHECKING USERNAME AND PASSWORD #####

    def test_check_password_correct(self):
        username = 'Stacey'
        password = 'sailboat'
        self.assertEqual(self.db.check_password(username,password),True)
    
    def test_check_password_incorrect(self):
        username = 'Stacey'
        password = 'sailboats'
        self.assertEqual(self.db.check_password(username,password),False)
    
    def test_check_if_user_exists_true(self):
        username = 'Freddy'
        self.assertEqual(self.db.check_if_user_exists(username),(True,2))

    def test_check_if_user_exists_false(self):
        username = 'Jo'
        self.assertEqual(self.db.check_if_user_exists(username),(False,None))
        
    def test_add_user(self):
        username = 'Jo'
        password = 'JoJo'
        self.assertEqual(self.db.add_user(username,password),None)
        self.assertEqual(self.db.check_if_user_exists(username),(True,3))
    
    ##### TESTS FOR ACTIONS WITH VOCAB LISTS #####
    
    def test_coll_user_vocab_lists_full(self):
        self.db.user_id = 1
        self.assertEqual(self.db.coll_user_vocab_lists(),[(1,'German',1,'every-day; beginner',1),(4,'Body Parts',2,'German;intermediate',1)])
    
    def test_coll_user_vocab_lists_empty(self):
        self.db.user_id = 3
        self.assertEqual(self.db.coll_user_vocab_lists(),[])
        
    def test_get_list_id(self):
        list_name = 'Colors'
        tags = 'French;colors; beginner'
        self.assertEqual(self.db.get_list_id(list_name,tags),2)
        
    def test_create_new_list(self):
        list_name = 'Colors'
        tags = 'Spanish; colors; easy'
        self.db.user_id = 2
        self.assertEqual(self.db.create_new_list(list_name,tags),None)
        self.assertEqual(self.db.coll_user_vocab_lists(),[(2,'Colors',1,'French;colors; beginner',2),(3,'Colors',2,'Arabic;colors; beginner',2),(5,'Colors',3,'Spanish; colors; easy',2)])
        
    def test_add_word(self):
        self.db.user_id = 1
        self.db.curr_list_id=4
        word = 'Zehe'
        meaning = 'toe'
        example = "Eine Zehe von meinem linken Fuß ist blau geworden; Die zehn Zehen von Baby Füßchen sind super klein und so süß vergleicht mit den von erwachsenen Füßen."
        tags = 'German; intermediate; funny; body; small'
        self.assertEqual(self.db.get_words(),[])
        self.assertEqual(self.db.add_word(word,meaning,example,tags),None)
        self.assertEqual(self.db.get_words(),[(10,'Zehe','toe',"Eine Zehe von meinem linken Fuß ist blau geworden; Die zehn Zehen von Baby Füßchen sind super klein und so süß vergleicht mit den von erwachsenen Füßen.",'German; intermediate; funny; body; small',4)])
    
if __name__ == '__main__':
    unittest.main()
