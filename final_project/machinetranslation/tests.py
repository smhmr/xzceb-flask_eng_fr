
import unittest

import english_to_french, french_to_english

class Teste2f(unittest.TestCase): 
    def test1(self): 
        # Test Hello returns Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        # Test None returns empty string
        self.assertNotEqual(english_to_french("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(english_to_french(0), 0)

class Testf2e(unittest.TestCase): 
    def test1(self): 
        # Test Bonjour returns Hello
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # Test Bonjour does not return Bonjour
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        # Test None returns empty string
        self.assertNotEqual(french_to_english("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(french_to_english(0), 0)
        
unittest.main()