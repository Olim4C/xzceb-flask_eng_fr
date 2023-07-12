import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'bonne nuit')

class TestfrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hi')
        self.assertNotEqual(frenchToEnglish('bonne nuit'), 'Hello')

unittest.main()