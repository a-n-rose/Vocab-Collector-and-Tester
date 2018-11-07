import unittest
from unittest.mock import patch
import input_manager
import vocab_collector
from errors import ExitApp

class VocabInputCheck(unittest.TestCase):

    def test_rem_space_specialchar_nospace_nospecialchar(self):
        user_input = 'Stacey'
        self.assertEqual(input_manager.rem_space_specialchar(user_input),'Stacey')
        
    def test_rem_space_specialchar_withspace_nospecialchar(self):
        user_input = 'S t a c e y'
        self.assertEqual(input_manager.rem_space_specialchar(user_input),'Stacey')
        
    def test_rem_space_specialchar_nospace_withspecialchar(self):
        user_input = '$()(S?@ta______c&!e+=y'
        self.assertEqual(input_manager.rem_space_specialchar(user_input),'Stacey')
        
    def test_rem_space_specialchar_noalphanumeric(self):
        user_input = '*#(!)  (# #&___$$(@ '
        self.assertEqual(input_manager.rem_space_specialchar(user_input),'')
        
    def test_rem_space_specialchar_empty(self):
        user_input = ''
        self.assertEqual(input_manager.rem_space_specialchar(user_input),'')
    
if __name__ == '__main__':
    unittest.main()
    
