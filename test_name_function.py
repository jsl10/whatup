import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        formatted_name=get_formatted_name('Jae','Lee')
        self.assertEqual(formatted_name,'Jae Lee')


    def test_fist_last_name(self):
	formatted_name=get_formatted_name('James','Kim')
	self.assertEqual(formatted_name,'James Kim')

unittest.main()
                                          
                                        
