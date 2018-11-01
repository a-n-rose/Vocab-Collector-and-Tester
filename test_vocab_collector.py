import unittest
import input_functions
from unittest.mock import patch


class UserInput(unittest.TestCase):
    
    #I'm still a newbie with mock so I don't completely understand this decorator. But, it seems to work... 
    @patch('input_functions.get_username',return_value='Harietta')
    def test_get_username_correct(self, input):
        self.assertEqual(input_functions.get_username(),'Harietta')
    
    @patch('input_functions.get_username',return_value='get_username()')
    def test_get_username_incorrect(self, input):
        self.assertEqual(input_functions.get_username(),input_functions.get_username())

    def test_username_correct(self):
        self.assertEqual(input_functions.prep_username('blubidy'),'blubidy')
        
    def test_username_empty(self):
        self.assertEqual(input_functions.prep_username(' '),None)
    
    def test_username_removechars(self):
        self.assertEqual(input_functions.prep_username('harYdIc*3**$&d d'),'harYdIc3dd')
        
    def test_username_novalidchars(self):
        self.assertEqual(input_functions.prep_username('  &$*@)~~ #*(@'),None)
        
        
if __name__ == '__main__':
    unittest.main()
    
