import unittest
from translator import englishtofrench, frenchtoenglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench("Hello"),"Bonjour")
        self.assertEqual(englishtofrench("Love"),"Amour")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")
        self.assertEqual(frenchtoenglish("Amour"),"Love")
unittest.main()