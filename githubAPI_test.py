from unittest import TestCase
import unittest

from githubAPI567_Atishay import Github

class TestGithub(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test1(self):
        self.assertEqual(Github('kdoskdowkdowkdowk'), False)
    def test2(self):
        self.assertEqual(Github('atishay2305-hub'), True)
        self.assertEqual(Github('sdsjdosjdosjdsd'), False)
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
